import logging
import pkg_resources

from pyramid.httpexceptions import HTTPFound
from pyramid.exceptions import NotFound
from pyramid.url import resource_url
from pyramid.view import view_config
from pyramid.renderers import render_to_response

from pylonshq.models import AppRoot

log = logging.getLogger(__name__)

class AppView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.ctx = self.request.tmpl_context
        self.ctx.active_header_nav = self.request.view_name or 'home'
        self.ctx.active_footer_nav = ''
        self.ctx.masthead_logo = 'pylons'
        self.ctx.pagename = 'Pylons Project'
    
    def render_page(self, section, redir_elems):
        subpath = self.request.subpath
        if not subpath:
            return HTTPFound(location=resource_url(self.context, self.request, *redir_elems))
        tmpl_path = 'templates/pages/%s/%s.mako' % (section, '/'.join(subpath))
        if pkg_resources.resource_exists('pylonshq', tmpl_path):
            self.ctx.active_footer_nav = '-'.join([self.request.view_name]+list(subpath))
            values = {}
            return render_to_response('pylonshq:%s' % tmpl_path, values, self.request)
        return NotFound()
    
    @view_config(name='', context=AppRoot, renderer='pylonshq:templates/home/home.mako')
    def home(self):
        return {}
    
    @view_config(name='pylons', context=AppRoot)
    def pylons(self):
        self.ctx.pagename = 'Pylons Project'
        return self.render_page('pylons', ('pylons','about'))
    
    @view_config(name='projects', context=AppRoot)
    def projects(self):
        self.ctx.pagename = 'Projects'
        if 'pyramid' in self.request.subpath:
            self.ctx.masthead_logo = 'pyramid'
        elif 'pylons-framework' in self.request.subpath:
            self.ctx.masthead_logo = 'pylonsfw'
        return self.render_page('projects', ('projects','pyramid','about'))
    
    @view_config(name='community', context=AppRoot)
    def community(self):
        self.ctx.pagename = 'Community'
        return self.render_page('community', ('community','how-to-participate'))
    
    @view_config(name='tools', context=AppRoot)
    def tools(self):
        self.ctx.pagename = 'Tools'
        return self.render_page('tools', ('tools','pastebins'))
        
    @view_config(name='test', context=AppRoot, renderer='pylonshq:templates/home/test.mako')
    def test(self):
        self.ctx.pagename = 'Test'
        return {}



