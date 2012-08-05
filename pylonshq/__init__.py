from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
import pyramid_beaker
import pyramid_sqla
import pyramid_handlers

from pylonshq.lib.security import groupfinder
from pylonshq.handlers import add_handlers
import pylonshq.lib.request as request
from pylonshq.lib.github3 import init_github

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

    # initialize database
    pyramid_sqla.add_engine(settings, prefix='sqlalchemy.')

    # configure beaker sessions
    session_factory = pyramid_beaker.session_factory_from_settings(settings)
    config.set_session_factory(session_factory)

    # configure beaker cache regions
    pyramid_beaker.set_cache_regions_from_settings(settings)

    # add i18n dirs
    config.add_translation_dirs('pylonshq:locale/')

    # initialize handlers
    config.include('pyramid_handlers')

    # initialize github client
    config.registry['github'] = init_github(settings)

    # configure renderers
    config.add_subscriber('pylonshq.lib.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
    config.add_subscriber('pylonshq.lib.subscribers.add_localizer',
                          'pyramid.events.ContextFound')
    config.add_static_view('static', 'pylonshq:static')

    # set up handlers
    config.include(add_handlers)

    # scan packages
    config.scan('pylonshq')

    return config.make_wsgi_app()
