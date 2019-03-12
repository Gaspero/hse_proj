# -*- coding: utf-8 -*-

from application import APP


@APP.route('/')
def hello():
    return 'Hello World!'
