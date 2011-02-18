# -*- coding: utf-8 -*- 
from pyramid.threadlocal import get_current_request
from pyramid.exceptions import ConfigurationError
from pyramid.url import route_url
from pyramid.url import current_route_url
from pyramid.i18n import get_localizer
from pyramid.i18n import TranslationStringFactory

from pylonshq import helpers

def add_renderer_globals(event):
    """ A subscriber to the ``pyramid.events.BeforeRender`` events.  Updates
    the :term:`renderer globals` with values that are familiar to Pylons
    users."""
    request = event.get('request')
    if request is None:
        request = get_current_request()
    globs = {
        'url': route_url,
        'current_url': current_route_url,
        'h': helpers,
    }
    if request is not None:
        tmpl_context = request.tmpl_context
        globs['c'] = tmpl_context
        globs['tmpl_context'] = tmpl_context
        globs['_'] = request.translate
        globs['localizer'] = request.localizer
        try:
            globs['session'] = request.session
        except ConfigurationError:
            pass
    event.update(globs)

tsf = TranslationStringFactory('pylonshq')

def add_localizer(event):
    request = event.request
    localizer = get_localizer(request)
    def auto_translate(string):
        return localizer.translate(tsf(string))
    request.localizer = localizer
    request.translate = auto_translate
