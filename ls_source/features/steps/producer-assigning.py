# -*- coding: utf-8 -*-
import requests
import logging
from models.customer import Customer
from models.producers import Producer
from models.order import Order
from behave import *


@given('a set of producers')
def step_1(context):
    for row in context.table:
        try:
            Producer.get(Producer.name == row['name'])
        except Producer.DoesNotExist:
            Producer.create(name=row['name'],
                            district=row['district'],
                            address=row['address'],
                            workers=row['workers'],
                            working_hours=row['working_hours'])


@given('an order')
def step_2(context):
    for row in context.table:
        try:
            context.customer_id = Customer.get(Customer.email=='test@test.com')
        except Customer.DoesNotExist:
            context.customer_id = Customer.create(email='test@test.com')
        context.order_id = Order.create(customer_id=context.customer_id,
                                        order_status=row['order_status'],
                                        district=row['district'])


@when('I confirm order')
def step_3(context):
    try:
        context.request = requests.put(f'http://127.0.0.1:5001/order/update/{str(context.order_id)}',
                                       json={"order_status": "Payment"},
                                       headers={'Content-Type': 'application/json'})
    except:
        context.request = False
    assert context.request.json()['isSuccess']


@then('System updates district of the order to {district}')
def step_4(context, district):
    order = Order.get(Order.order_id == context.order_id)
    assert order.district == district
