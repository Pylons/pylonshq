from pylons.views import action

from pylonshq.models import DBSession
from pylonshq.models import MyModel

class MyHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='mytemplate.mak')
    def index(self):
        root = MyModel.by_name('root')
        return {'root':root, 'project':'pylonshq'}
