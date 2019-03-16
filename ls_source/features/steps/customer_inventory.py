# -*- coding: utf-8 -*-

import sys

from behave import given, when, then

try:
    sys.path.remove('')
    from models.category import Category
    from models.product import Product
except ValueError:
    pass
else:
    sys.path.append('/Users/ivanshadrin/PycharmProjects/hse_proj/ls_source')


#sys.path.append('/Users/ivanshadrin/PycharmProjects/hse_proj/ls_source')
#from models.category import Category
#from models.product import Product




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

#
# @when('we search for items with category "Book"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass
#
#
# @when("we search for items with lowest price")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass
#
#
# @then('we will get info for 1 items with name "Harry Potter"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass
#
#
# @then("we will find 2 Book items")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass
