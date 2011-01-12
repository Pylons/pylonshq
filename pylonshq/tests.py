import unittest

from pyramid import testing
from pyramid.request import TemplateContext

class AppViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
    
    def _makeOne(self, context, request):
        from pylonshq.views import AppView
        return AppView(context, request)

    def test_home(self):
        context = testing.DummyResource()
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        view = self._makeOne(context, request)
        home = view.home()
        self.assertEqual(view.ctx.pagename, 'Home')
    
    def test_pylons(self):
        context = testing.DummyResource()
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        view = self._makeOne(context, request)
        home = view.pylons()
        self.assertEqual(view.ctx.pagename, 'Pylons Project')
    
    def test_projects(self):
        context = testing.DummyResource()
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        view = self._makeOne(context, request)
        home = view.projects()
        self.assertEqual(view.ctx.pagename, 'Projects')
    
    def test_community(self):
        context = testing.DummyResource()
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        view = self._makeOne(context, request)
        home = view.community()
        self.assertEqual(view.ctx.pagename, 'Community')
    
    def test_tools(self):
        context = testing.DummyResource()
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        view = self._makeOne(context, request)
        home = view.tools()
        self.assertEqual(view.ctx.pagename, 'Tools')
    
    def test_test(self):
        context = testing.DummyResource()
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        view = self._makeOne(context, request)
        home = view.test()
        self.assertEqual(view.ctx.pagename, 'Test')
