# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from datetime import timedelta
import pkg_resources

from pyramid.httpexceptions import HTTPFound
from pyramid.exceptions import NotFound
from pyramid.url import route_url
from pyramid.renderers import render_to_response
from pyramid.response import Response

from pyramid_handlers import action
from pylonshq.handlers.base import BaseHandler as base

from beaker.cache import cache_region

from operator import attrgetter
import feedparser
from docutils.core import publish_parts

log = logging.getLogger(__name__)


class PageHandler(base):

    def __init__(self, request):
        base.__init__(self, request)
        self.endpath = self.request.matchdict.get('endpath', None)

    def render_page(self, section, redirpath, values=None):
        if self.endpath is None:
            return HTTPFound(
                location=route_url(
                    'subsections',
                    self.request,
                    action=section,
                    endpath='/'.join(redirpath)
                ))
        self.c.active_footer_nav = '-'.join(
            [self.request.matchdict.get('action')]
            +list(self.endpath))
        for ext in ('.mako', '.rst'):
            tmpl_path = ('templates/pages/%s/%s%s' % (
                section,
                '/'.join(self.endpath),
                ext))
            values = values or {}
            if pkg_resources.resource_exists('pylonshq', tmpl_path):
                if ext == '.mako':
                    return render_to_response(
                        'pylonshq:%s' % tmpl_path, values, self.request)
                else:
                    self.c.pagename = ' : '.join(
                        [item.replace('-', ' ').title() for item in self.endpath])
                    content = pkg_resources.resource_string(
                        'pylonshq',
                        tmpl_path)
                    body = publish_parts(
                        content,
                        writer_name='html')['html_body']
                    values={'body':body}
                    return render_to_response(
                        'pylonshq:templates/rst.mako', values, self.request)
        raise NotFound()

    @cache_region('long_term')
    @action()
    def freenode_ver(self):
        return Response('jdf*hnm1?')

    @action(renderer='pylonshq:templates/home/home.mako')
    def index(self):
        self.c.pagename = 'Home'

        @cache_region('moderate_term')
        def _inside():
            content = pkg_resources.resource_string(
                'pylonshq', 'templates/home/inside.rst')
            body = publish_parts(
                content,
                writer_name='html')['html_body']
            return body

        @cache_region('moderate_term')
        def _discussions():
            rss_urls = (
                'https://groups.google.com/forum/feed/pylons-discuss/msgs/atom.xml?num=50',
                'https://groups.google.com/forum/feed/pylons-devel/msgs/atom.xml?num=50'
            )
            feeds = [feedparser.parse(rss_url) for rss_url in rss_urls]
            _entries = []
            for feed in feeds:
                _entries.extend(feed[ "items" ])
            _ordered = sorted(
                (_entry for _entry in _entries),
                key=attrgetter('date_parsed'),
                reverse=True
            )
            entries = [dict(
                title = entry.title,
                link = entry.link,
                author = entry.author_detail.get('name', '-'),
                updated = (
                    datetime(*entry.updated_parsed[:6])-timedelta(hours=5)
                ).strftime('%b %d, %H:%M')
            ) for pos, entry in enumerate(_ordered) if _ordered and pos < 10]
            return entries

        @cache_region('moderate_term')
        def _projects():
            github = self.request.registry.get('github')
            try:
                org = github.get_organization(
                    self.request.registry.settings.get('github.username'))
                all_projects = org.get_repos()
                ordered = sorted(
                    (project for project in all_projects
                        if project.pushed_at is not None),
                    key=attrgetter('pushed_at'),
                    reverse=True
                    )
                return [ordered[i] for i in xrange(20)]
            except:
                return []

        return {
            'inside': _inside(),
            'discussions': _discussions(),
            'projects': _projects()
        }

    @action()
    def about(self):
        self.c.pagename = 'About'
        return self.render_page('about', ('pylons',))

    @action()
    def projects(self):
        self.c.pagename = 'Projects'
        redirpath = None
        values = {}

        @cache_region('long_term')
        def _downloads(repo):
            from pylonshq.lib.utils import natural
            github = self.request.registry.get('github')
            try:
                org = github.get_organization(
                    self.request.registry.settings.get('github.username'))
                repo = org.get_repo(repo)
                all_downloads = repo.get_tags()
                return [
                    d for d in sorted(
                        all_downloads,
                        key=attrgetter('name'),
                        reverse=True
                        )
                    if not d.name.startswith('0') \
                        and d.name.find('a') == -1 \
                        and d.name.find('b') == -1
                        ]
                return all_downloads
            except:
                return []

        pyramid_redirpath = ('pyramid','about',)
        if self.endpath is not None:
            if 'pyramid' in self.endpath:
                if len(self.endpath)==1:
                    self.endpath = None
                    redirpath = pyramid_redirpath
                self.c.masthead_logo = 'pyramid'
                values['downloads'] = _downloads('pyramid')
            elif 'pylons-framework' in self.endpath:
                if len(self.endpath) == 1:
                    self.endpath = None
                    redirpath = ('pylons-framework','about',)
                self.c.masthead_logo = 'pylonsfw'
                values['downloads'] = _downloads('pylons')
        else:
            redirpath = pyramid_redirpath
        return self.render_page('projects', redirpath, values)

    @action()
    def community(self):
        self.c.pagename = 'Community'
        return self.render_page('community', ('how-to-participate',),)

    @action()
    def tools(self):
        self.c.pagename = 'Tools'
        return self.render_page('tools', ('pastebins',))

    @action(renderer='pylonshq:templates/home/test.mako', permission='edit')
    def test(self):
        self.c.pagename = 'Test'
        hello = self.request.translate('Hello')
        print hello
        return {}

