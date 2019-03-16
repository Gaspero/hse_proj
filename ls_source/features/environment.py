# -*- coding: utf-8 -*-

import os
import tempfile
from behave import fixture, use_fixture

from application import APP
# from flask import app as APP


@fixture
def flaskr_client(context, *args, **kwargs):
    context.db, APP.config['DATABASE'] = tempfile.mkstemp()
    APP.testing = True
    context.client = APP.test_client()

    with APP.app_context():
        # init_db()
        pass
    yield context.client

    # -- CLEANUP:
    os.close(context.db)
    os.unlink(APP.config['DATABASE'])


def before_feature(context, feature):
    # -- HINT: Recreate a new flask client before each feature is executed.
    context.config.setup_logging()
    use_fixture(flaskr_client, context)
