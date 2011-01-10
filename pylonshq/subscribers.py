from pyramid.threadlocal import get_current_request
from pyramid.exceptions import ConfigurationError
from pyramid.url import resource_url
from pylonshq import helpers

def add_renderer_globals(event):
    request = event.get('request')
    if request is None:
        request = get_current_request()
    globs = {
        'url': resource_url,
        'h':helpers,
    }
    if request is not None:
        tmpl_context = request.tmpl_context
        globs['ctx'] = tmpl_context
        try:
            globs['session'] = request.session
        except ConfigurationError:
            pass
    event.update(globs)


