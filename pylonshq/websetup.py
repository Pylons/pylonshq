import logging

import pyramid_sqla as psa
import transaction

import sqla
import sqla.models as models

def setup_app(command, conf, vars):
    # Initialize logging
    command.logging_file_config(conf.filename)
    log = logging.getLogger(__name__)

    # Load the application
    app = sqla.main(conf.global_conf, **conf.local_conf)
    #settings = app.registry.settings

    # Abort if any table exists
    for table in models.Base.metadata.sorted_tables:
        log.debug("checking if table '%s' exists", table.name)
        if table.exists():
            raise RuntimeError("database table '%s' exists"  % table.name)

    # Create all tables
    models.Base.metadata.create_all()
    sess = models.Session()

    # Record 1
    #p = models.Page(title="FrontPage", content="Edit me.")
    #sess.add(p)

    transaction.commit()
