from pyramid.config import Configurator
import pyramid_beaker
import pyramid_sqla
import pyramid_handlers
import pylonshq.lib.request as request
#from pyramid_sqla.static import add_static_route

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          request_factory=request.PylonsHQRequest
                          )
    
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
    
    # Configure renderers
    #config.add_renderer('.html', 'pyramid.mako_templating.renderer_factory')
    config.add_subscriber('pylonshq.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
    config.add_subscriber('pylonshq.subscribers.add_localizer',
                          'pyramid.events.NewRequest')
    config.add_static_view('static', 'pylonshq:static')
    # Set up routes and views
    config.add_handler('home', '/', 'pylonshq.handlers:MainHandler',
                       action='index')
    config.add_handler('sections', '/{action}', handler='pylonshq.handlers:MainHandler')
    config.add_handler('subsections', '/{action}/*endpath', handler='pylonshq.handlers:MainHandler')
    #config.add_handler('main', '/{action}', 'pylonshq.handlers:MainHandler',
    #    path_info=r'/(?!favicon\.ico|robots\.txt|w3c)')
    #add_static_route(config, 'pylonshq', 'static', cache_max_age=3600)
    config.scan('pylonshq')
    return config.make_wsgi_app()
