# -*- coding: utf-8 -*-
from models.product import Product, ProductIngredient
from behave import *


@given('a set of products')
def step_1(context):
    for row in context.table:
        try:
            Product.get(Product.name == row['name'])
        except Product.DoesNotExist:
            Product.create(name=row['name'],
                           price=row['price'],
                           description=row['description'])


@when('I sort products by price ascending')
def step_2(context):
    context.result = Product.sort_by_price(direction='asc')
    assert context.result


@then('System returns the following set')
def step3(context):
    for index, row in enumerate(context.table):
        assert row['name'] == context.result[index].name
