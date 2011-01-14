import unittest

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
        request = DummyRequest()
        handler = self._makeOne(request)
        info = handler.index()
        self.assertEqual(info['project'], 'sqla')

class DummyRequest(object):
    pass
