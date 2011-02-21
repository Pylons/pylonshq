# -*- coding: utf-8 -*- 
import logging

import sqlalchemy as sa

from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid import security

from pyramid_handlers import action
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from pylonshq.handlers.base import BaseHandler as base

log = logging.getLogger(__name__)

        
class ShowcaseHandler(base):
    
    @action(renderer='pylonshq:templates/home/test.mako')
    def index(self):
        return {}