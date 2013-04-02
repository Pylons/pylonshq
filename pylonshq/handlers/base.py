# -*- coding: utf-8 -*- 
import logging

from pyramid.view import view_config
from pyramid.security import authenticated_userid

log = logging.getLogger(__name__)


class BaseHandler(object):
    def __init__(self, request):
        self.request = request
        self.logged_in = authenticated_userid(request)
        self.c = self.request.tmpl_context
        active_header_nav = 'home'
        if request.matchdict is not None:
             active_header_nav = self.request.matchdict.get(
                'action', active_header_nav)
        self.c.active_header_nav = active_header_nav
        self.c.active_footer_nav = ''
        self.c.masthead_logo = 'pylons'
        self.c.pagename = ''


class ExceptionViews(BaseHandler):

    @view_config(context='pyramid.exceptions.NotFound',
                 renderer='pylonshq:templates/error.mako')
    def notfound(self):
        self.request.response_status = '404 Not Found'
        return {
            'number': '404',
            'error': 'PAGE NOT FOUND',
            'message': 'The page you\'re looking for isn\'t here.'
        }

