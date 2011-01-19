from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid
from pylonshq.models import User

class PylonsHQRequest(Request):
    @reify
    def user(self):
        if not self.path_info.startswith('/static'):
            return User.by_user_name(unauthenticated_userid(self))