# -*- coding: utf-8 -*-

import logging

from datetime import datetime
from peewee import *

from application import DB
from models.customer import Customer
from models.product import Product, ProductAdditional
from models.producers import Producer

"""
STATUSES = ((1, 'Pre-Order'),
            (2, 'Payment'),
            (3, 'Paid'),
            (4, 'Formation'),
            (5, 'Delivery'),
            (6, 'Performed'))
"""


class Order(DB.Model):
    order_id = PrimaryKeyField()
    customer_id = ForeignKeyField(Customer, to_field='customer_id', null=False)
    order_status = CharField(default="Pre-Order", null=False)
    create_time = DateTimeField(default=datetime.now, null=False)
    district = CharField(50, null=True)
    producer_id = ForeignKeyField(Producer, to_field='producer_id', null=True)  # TODO: сделать присвоение на опр. этапе

    class Meta:
        table_name = 'orders'

    # метод для получения продюсеров, подходящих заказу по району
    def find_producers(self):
        query = Producer.select().where(Producer.district == self.district)
        return query if query else None  # else 'No producers available'


class OrderItem(DB.Model):
    item_id = PrimaryKeyField()
    order_id = ForeignKeyField(Order, backref='items')
    product_id = ForeignKeyField(Product, to_field='product_id', null=False)
    # list_price = FloatField(default=0, null=False) ???
    quantity = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'order_items'
