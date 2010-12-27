from pyramid.view import view_config
from pylonshq.models import MyModel

@view_config(context=MyModel, renderer='pylonshq:templates/mytemplate.pt')
def my_view(request):
    return {'project':'pylonshq'}
