import logging
from datetime import datetime
from datetime import timedelta
import pkg_resources

from pyramid.httpexceptions import HTTPFound
from pyramid.exceptions import NotFound
from pyramid.url import route_url
from pyramid.renderers import render_to_response

from pyramid_handlers import action
from pylonshq.handlers.base import BaseHandler as base

from beaker.cache import cache_region

from docutils.core import publish_parts

log = logging.getLogger(__name__)

        
class PageHandler(base):
    
    def render_page(self, section, redir_elems, values=None):
        endpath = self.request.matchdict.get('endpath', None)
        if not endpath:
            return HTTPFound(
                location=route_url(
                    'subsections',
                    self.request,
                    action=section,
                    endpath='/'.join(redir_elems)
                ))
        self.c.active_footer_nav = '-'.join(
            [self.request.matchdict.get('action')]
            +list(endpath))
        for ext in ('.mako', '.rst'):
            tmpl_path = ('templates/pages/%s/%s%s' % (
                section,
                '/'.join(endpath),
                ext))
            values = values or {}
            if pkg_resources.resource_exists('pylonshq', tmpl_path):
                if ext == '.mako':
                    return render_to_response(
                        'pylonshq:%s' % tmpl_path, values, self.request)
                else:
                    self.c.pagename = ' : '.join(
                        [item.replace('-', ' ').title() for item in endpath])
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
    
    @action(renderer='pylonshq:templates/home/home.mako')
    def index(self):
        self.c.pagename = 'Home'
        @cache_region('moderate_term')
        def _discussions():
            import feedparser
            d = feedparser.parse(
                'http://groups.google.com/group/pylons-discuss/feed/atom_v1_0_msgs.xml'
            )
            entries = [dict(
                title = entry.title,
                link = entry.link,
                author = entry.author_detail.name,
                updated = (
                    datetime(*entry.updated_parsed[:6])-timedelta(hours=5)
                ).strftime('%b %d, %H:%M')
            ) for pos, entry in enumerate(d['entries']) if pos < 10]
            return entries
        @cache_region('moderate_term')
        def _projects():
            from operator import attrgetter
            github = self.request.registry.get('github')
            all_projects = github.repos.list(
                self.request.registry.settings.get('github.username')
            )
            ordered = sorted(
                (project for project in all_projects),
                key=attrgetter('pushed_at'),
                reverse=True
            )
            return [ordered[i] for i in xrange(20)]
        return {
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
        values = {}
        endpath = self.request.matchdict.get('endpath')
        @cache_region('long_term')
        def _downloads(repo):
            from pylonshq.lib.utils import natural
            github = self.request.registry.get('github')
            all_downloads = github.repos.tags('Pylons/%s' % repo)
            return [
                d for d in sorted(all_downloads, key=natural)
                if not d.startswith('0') and d.find('a') == -1
            ]
        if endpath is not None:
            if 'pyramid' in endpath:
                self.c.masthead_logo = 'pyramid'
                values['downloads'] = _downloads('pyramid')
            elif 'pylons-framework' in endpath:
                self.c.masthead_logo = 'pylonsfw'
                values['downloads'] = _downloads('pylons')
        return self.render_page('projects', ('pyramid','about',), values)

    @action()
    def community(self):
        self.c.pagename = 'Community'
        return self.render_page('community', ('how-to-participate',),)
    
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

