
def add_handlers(config):
    config.add_handler('home', '/', 'pylonshq.handlers.pages:PageHandler',
                       action='index')
    config.add_handler('freenode', '/freenode.ver', 'pylonshq.handlers.pages:PageHandler',
                       action='freenode_ver')
    config.add_handler('login', '/login', 
                        handler='pylonshq.handlers.accounts:AccountHandler',
                        action='login')
    config.add_handler('logout', '/logout',
                        handler='pylonshq.handlers.accounts:AccountHandler',
                        action='logout')
    config.add_handler('jobs', '/jobs',
                        handler='pylonshq.handlers.jobs:JobsHandler',
                        action='index')
    config.add_handler('jobs_actions', '/jobs/{action}/*endpath',
                        handler='pylonshq.handlers.jobs:JobsHandler')
    config.add_handler('showcase', '/showcase',
                        handler='pylonshq.handlers.showcase:ShowcaseHandler',
                        action='index')
    config.add_handler('showcase_actions', '/showcase/{action}/*endpath',
                        handler='pylonshq.handlers.showcase:ShowcaseHandler')
    config.add_handler('sections', '/{action}',
                        handler='pylonshq.handlers.pages:PageHandler')
    config.add_handler('subsections', '/{action}/*endpath',
                        handler='pylonshq.handlers.pages:PageHandler')