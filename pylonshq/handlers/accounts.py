# -*- coding: utf-8 -*- 
import logging

import sqlalchemy as sa

from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid.view import view_config
from pyramid import security

from pyramid_handlers import action
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from pylonshq.handlers.base import BaseHandler as base
from pylonshq.models import User
from pylonshq.forms import LoginForm

log = logging.getLogger(__name__)

      
class AccountHandler(base):
    
    @view_config(renderer='pylonshq:templates/home/login.mako',
        context='pyramid.exceptions.Forbidden')
    @action(renderer='pylonshq:templates/home/login.mako')
    def login(self):
        if self.logged_in:
            self.request.session.flash('You are already connected!', queue='notice')
            return HTTPFound(
                location=self.request.route_url('home')
            )
        self.c.pagename = 'Login'
        self.c.active_header_nav = 'tools'
        self.c.active_footer_nav = 'tools-login'
        params = self.request.params
        form = Form(self.request, schema=LoginForm, obj=params)
        if form.validate():
            form.bind(params)
            #clear the cache for user
            User.by_username(params.get('username'), invalidate=True)
            user = User.by_username(params.get('username'), cache=None)
            if user:
                password = params.get('password')
                if user.password == User.pass_crypt(password)\
                and user.status == 1:
                    user.last_login_date = sa.func.now()
                    self.request.session.flash(u'Welcome back %s !' % user.username, queue='success')
                    headers = security.remember(self.request,
                                                user.username)
                    return HTTPFound(location=self.request.route_url('home'),
                                     headers=headers)
            self.request.session.flash(u'Wrong username or password!', queue='notice')
        return {
            'item': params,
            'form': FormRenderer(form)
        }
    
    def logout(self):
        if not self.logged_in:
            self.request.session.flash('You are not connected!', queue='notice')
            return HTTPFound(
                location=self.request.route_url('home')
            )
        headers = security.forget(self.request)
        self.request.session.flash('You have been logged out!', queue='success')
        return HTTPFound(location=self.request.route_url('home'),
                         headers=headers)