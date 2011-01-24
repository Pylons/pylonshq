import logging
import pkg_resources

import sqlalchemy as sa
import pyramid.security

from pylonshq.models import User
from pyramid.httpexceptions import HTTPFound
from pyramid.exceptions import NotFound
from pyramid.url import route_url
from pyramid.view import view_config
from pyramid.renderers import render_to_response

from pyramid_handlers import action

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
            return HTTPFound(location=route_url('subsections',
                                                self.request,
                                                action=section,
                                                endpath='/'.join(redir_elems)))
        tmpl_path = 'templates/pages/%s/%s.mako' % (section, '/'.join(endpath))
        if pkg_resources.resource_exists('pylonshq', tmpl_path):
            self.c.active_footer_nav = '-'.join([self.request.matchdict.get('action')]
                                                +list(endpath))
            values = {}
            return render_to_response('pylonshq:%s' % tmpl_path,
                                      values,
                                      self.request)
        raise NotFound()
    
    @view_config(context='pyramid.exceptions.NotFound',
                 renderer='pylonshq:templates/404.mako')
    def notfound(self):
        return {}
    
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
        hello = self.request.translate('Hello')
        print hello
        return {}
    
    def sign_in(self):
        #clear the cache for user
        User.by_user_name(self.request.params.get('user_name'), invalidate=True)
        user = User.by_user_name(self.request.params.get('user_name'), cache=None)
        if user:
            password = self.request.params.get('password')
            if user.user_password == User.pass_crypt(password)\
            and user.status == 1:
                user.last_login_date = sa.func.now()
                self.request.session.flash(u'Signed in successfully')
                headers = pyramid.security.remember(self.request,
                                                    user.user_name)
                return HTTPFound(location=self.request.route_url('home'),
                                 headers=headers)

        self.request.session.flash(u'Wrong username or password', 'warning')
        return HTTPFound(location=self.request.route_url('home'))
    
    def sign_out(self):
        headers = pyramid.security.forget(self.request)
        return HTTPFound(location=self.request.route_url('home'),
                         headers=headers)