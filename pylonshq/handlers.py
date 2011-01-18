import logging

import logging
import pkg_resources

from pyramid.httpexceptions import HTTPFound
from pyramid.exceptions import NotFound
from pyramid.url import route_url
from pyramid_handlers import action
from pyramid.renderers import render_to_response

#from sqla.models import MyModel

log = logging.getLogger(__name__)
        
class MainHandler(object):
    def __init__(self, request):
        self.request = request
        self.c = self.request.tmpl_context
        self.c.active_header_nav = self.request.matchdict.get('action') or 'home'
        self.c.active_footer_nav = ''
        self.c.masthead_logo = 'pylons'
        self.c.pagename = ''
    
    def render_page(self, section, redir_elems):
        endpath = self.request.matchdict.get('endpath', None)
        if not endpath:
            return HTTPFound(location=route_url('subsections', self.request, action=section, endpath='/'.join(redir_elems)))
        tmpl_path = 'templates/pages/%s/%s.mako' % (section, '/'.join(endpath))
        if pkg_resources.resource_exists('pylonshq', tmpl_path):
            self.c.active_footer_nav = '-'.join([self.request.matchdict.get('action')]+list(endpath))
            values = {}
            return render_to_response('pylonshq:%s' % tmpl_path, values, self.request)
        raise NotFound()
    
    @action(renderer='pylonshq:templates/home/home.mako')
    def index(self):
        self.c.pagename = 'Home'
        return {}
    
    @action()
    def pylons(self):
        self.c.pagename = 'Pylons Project'
        return self.render_page('pylons', ('about',))
    
    @action()
    def projects(self):
        self.c.pagename = 'Projects'
        endpath = self.request.matchdict.get('endpath')
        if endpath is not None:
            if 'pyramid' in endpath:
                self.c.masthead_logo = 'pyramid'
            elif 'pylons-framework' in endpath:
                self.c.masthead_logo = 'pylonsfw'
        return self.render_page('projects', ('pyramid','about',))
    
    @action()
    def community(self):
        self.c.pagename = 'Community'
        return self.render_page('community', ('how-to-participate',))
    
    @action()
    def tools(self):
        self.c.pagename = 'Tools'
        return self.render_page('tools', ('pastebins',))
        
    @action(renderer='pylonshq:templates/home/test.mako')
    def test(self):
        self.c.pagename = 'Test'
        return {}
    