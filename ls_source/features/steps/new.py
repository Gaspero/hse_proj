# -*- coding: utf-8 -*-

import requests
from behave import given, when, then


@given('a set of items in category')
def step_impl(context):
    for row in context.table:
        Category.get_or_create(name=row['name'])


@given('a set of items in inventory')
def step_impl(context):
    for row in context.table:
        try:
            Product.get(Product.name == row['name'])
        except Product.DoesNotExist:
            Product.create(name=row['name'],
                           price=row['price'],
                           category_id=row['category_id'])


@when('we search for items with name "{name}"')
def step_impl(context, name):
    try:
        context.result = Product.select().where(Product.name == name)
    except Product.DoesNotExist:
        context.result = None
    assert context.result is not None


@then('we will find {count:d} Book items')
def step_impl(context, count):
    assert context.result.count() == count
