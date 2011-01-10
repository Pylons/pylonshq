from persistent import Persistent
from persistent.mapping import PersistentMapping

from pyramid.security import Allow
from pyramid.security import Everyone

class AppRoot(PersistentMapping):
    __parent__ = __name__ = None
    __acl__ = [(Allow, Everyone, 'view')]


def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        app_root = AppRoot()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
