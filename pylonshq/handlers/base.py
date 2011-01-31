import logging

from pyramid.view import view_config
from pyramid_handlers import action

log = logging.getLogger(__name__)


class BaseHandler(object):
    def __init__(self, request):
        self.request = request
        self.c = self.request.tmpl_context
        self.c.active_header_nav = self.request.matchdict.get('action') or 'home'
        self.c.active_footer_nav = ''
        self.c.masthead_logo = 'pylons'
        self.c.pagename = ''


class ExceptionViews(BaseHandler):

    @view_config(context='pyramid.exceptions.NotFound',
                 renderer='pylonshq:templates/404.mako')
    def notfound(self):
        return {}