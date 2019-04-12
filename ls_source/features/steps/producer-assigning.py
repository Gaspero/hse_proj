# -*- coding: utf-8 -*-
import requests
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
        # Делаем запрос к API для изменения статуса ордера
        context.request = requests.put(f'http://127.0.0.1:5001/order/update/{str(context.order_id)}',
                                       json={"order_status": "Payment"},
                                       headers={'Content-Type': 'application/json'})
    except:
        context.request = False
    # Проверяем наличие ответа от сервера
    assert context.request.json()['isSuccess']


@then('System sets producer for given order to {name}')
def step_4(context, name):
    order = Order.get(Order.order_id == context.order_id)
    producer = Producer.get(Producer.name == name)
    assert order.producer_id == producer


@then('Producer for given order is not provided')
def step_5(context):
    order = Order.get(Order.order_id == context.order_id)
    # assert hasattr(order, 'producer_id') is False
    assert order.producer_id is None


@then('Order status is {status}')
def step_6(context, status):
    order = Order.get(Order.order_id == context.order_id)
    assert order.order_status == status
