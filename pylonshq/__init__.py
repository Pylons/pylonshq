from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
import pyramid_beaker
import pyramid_sqla
import pyramid_handlers

import pylonshq.lib.request as request
from pylonshq.security import groupfinder
from pylonshq.lib.github import init_github

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    
    # add policies
    authentication_policy = AuthTktAuthenticationPolicy('pyramidhq_seekrit',
                                                        callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          request_factory=request.PylonsHQRequest)
    
    # Initialize database
    pyramid_sqla.add_engine(settings, prefix='sqlalchemy.')

    # Configure Beaker sessions
    session_factory = pyramid_beaker.session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    
    # Configure Beaker cache regions
    pyramid_beaker.set_cache_regions_from_settings(settings)
    
    # Add i18n dirs
    config.add_translation_dirs('pylonshq:locale/')
    
    # Initialize handlers
    config.include('pyramid_handlers')
    
    # Initialize github client
    config.registry['github'] = init_github(settings)
    
    # Configure renderers
    config.add_subscriber('pylonshq.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
    config.add_subscriber('pylonshq.subscribers.add_localizer',
                          'pyramid.events.NewRequest')
    config.add_static_view('static', 'pylonshq:static')
    # Set up routes and views
    config.add_handler('home', '/', 'pylonshq.handlers.pages:PageHandler',
                       action='index')
    config.add_handler('login', '/login', 
                        handler='pylonshq.handlers.accounts:AccountHandler',
                        action='login')
    config.add_handler('logout', '/logout',
                        handler='pylonshq.handlers.accounts:AccountHandler',
                        action='logout')
    config.add_handler('sections', '/{action}',
                        handler='pylonshq.handlers.pages:PageHandler')
    config.add_handler('subsections', '/{action}/*endpath',
                        handler='pylonshq.handlers.pages:PageHandler')
    config.scan('pylonshq')
    return config.make_wsgi_app()
