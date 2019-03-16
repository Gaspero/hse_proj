# -*- coding: utf-8 -*-
import os
from behave import when, then

os.getcwd()

@when('i call categories')
def get_categories(context):
    context.page = context.client.get('/category/get', follow_redirects=True)
    assert context.page


@then('i should see "{count}" records')
def check_list_of_categories(context, count):
    js = context.page.get_json()
    assert int(count) == len(js['result'])
