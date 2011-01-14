import logging

from pyramid.view import view_config

class MainViews(object):
    def __init__(self, request):
        self.request = request
        self.c = self.request.tmpl_context
        self.c.active_header_nav = self.request.view_name or 'home'
        self.c.active_footer_nav = ''
        self.c.masthead_logo = 'pylons'
        self.c.pagename = ''
        
    @view_config(context='pyramid.exceptions.NotFound', renderer='pylonshq:templates/404.mako')
    def notfound(self):
        return {}