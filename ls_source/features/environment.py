# -*- coding: utf-8 -*-

import os
from behave import fixture, use_fixture

from application import APP
from models import init_models
from flask_peewee.db import Database


@fixture
def flaskr_client(context, *args, **kwargs):
    APP.config['DATABASE'] = {'engine': 'peewee.SqliteDatabase', 'name': ':memory:'}
    # context.db, APP.config['DATABASE'] = tempfile.mkstemp()
    APP.testing = True
    context.client = APP.test_client()

    with APP.app_context():
        DB = Database(APP)
        init_models(DB)
        # pass
    yield context.client

    # -- CLEANUP:
    # os.close(context.db)
    # os.unlink(APP.config['DATABASE'])


def before_feature(context, feature):
    # -- HINT: Recreate a new flask client before each feature is executed.
    context.config.setup_logging()
    use_fixture(flaskr_client, context)

# TODO: не работает. судя по всему, нужно адаптировать приложение для работы с application factories
