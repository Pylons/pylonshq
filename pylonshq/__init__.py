from pyramid.config import Configurator
import pyramid_beaker
import pyramid_sqla
from pyramid_sqla.static import add_static_route

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # Initialize database
    pyramid_sqla.add_engine(settings, prefix='sqlalchemy.')

    # Configure Beaker sessions
    session_factory = pyramid_beaker.session_factory_from_settings(settings)
    config.set_session_factory(session_factory)

    # Configure renderers
    #config.add_renderer('.html', 'pyramid.mako_templating.renderer_factory')
    config.add_subscriber('pylonshq.subscribers.add_renderer_globals',
                          'pyramid.events.BeforeRender')
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
