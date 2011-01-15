import unittest

from pyramid import testing
from pyramid.request import TemplateContext

class MyHandlerTests(unittest.TestCase):
    def setUp(self):
        from pyramid.config import Configurator
        import pyramid_sqla
        self.engine = pyramid_sqla.add_engine(url='sqlite://')
        self.session = pyramid_sqla.get_session()()
        self.config = Configurator(autocommit=True)
        self.config.begin()
        # Must call ``self.config.begin()`` in tests before using config.

    def tearDown(self):
        import pyramid_sqla
        self.config.end()
        # After calling ``self.config.end()``, don't use config.
        self.session = None
        pyramid_sqla.reset()

    def _makeOne(self, request):
        from pylonshq.handlers import MainHandler
        return MainHandler(request)
    
    def test_index(self):
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        handler = self._makeOne(request)
        page = handler.index()
        self.assertEqual(handler.c.pagename, 'Home')
    
    #def test_pylons(self):
    #    request = testing.DummyRequest(tmpl_context=TemplateContext)
    #    handler = self._makeOne(request)
    #    page = handler.pylons()
    #    self.assertEqual(page.c.pagename, 'Pylons Project')
    
    #def test_projects(self):
    #    request = testing.DummyRequest(tmpl_context=TemplateContext)
    #    handler = self._makeOne(request)
    #    page = handler.projects()
    #    self.assertEqual(handler.c.pagename, 'Projects')
    
    #def test_community(self):
    #    request = testing.DummyRequest(tmpl_context=TemplateContext)
    #    handler = self._makeOne(request)
    #    page = handler.community()
    #    self.assertEqual(handler.c.pagename, 'Community')
    
    #def test_tools(self):
    #    request = testing.DummyRequest(tmpl_context=TemplateContext)
    #    handler = self._makeOne(request)
    #    page = handler.tools()
    #    self.assertEqual(handler.c.pagename, 'Tools')
    
    def test_test(self):
        request = testing.DummyRequest(tmpl_context=TemplateContext)
        handler = self._makeOne(request)
        page = handler.test()
        self.assertEqual(handler.c.pagename, 'Test')

class DummyRequest(object):
    pass
