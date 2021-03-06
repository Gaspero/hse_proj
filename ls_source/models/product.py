# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *

from application import DB
from models.category import Category


class Product(DB.Model):
    product_id = PrimaryKeyField()
    name = CharField(unique=True, null=False)
    price = FloatField(default=0, null=False)
    # available_quantity = IntegerField(default=0, null=False)
    create_time = DateTimeField(default=datetime.now, null=False)
    description = CharField(null=False)
    size = CharField(null=True)
    weight = FloatField(null=True)
    energy = FloatField(null=True)
    proteins = FloatField(null=True)
    fat = FloatField(null=True)
    carbons = FloatField(null=True)
    category_id = ForeignKeyField(Category, to_field='category_id', null=True)

    class Meta:
        table_name = 'products'

    def __str__(self):
        return self.name

    @classmethod
    def sort_by_price(cls, direction):
        if direction == 'asc' or direction is None:
            result = cls.select().order_by(cls.price.asc())
        if direction == 'desc':
            result = cls.select().order_by(cls.price.desc())
        return result


class ProductAdditional(DB.Model):
    product_additional_id = PrimaryKeyField()
    name = CharField(unique=True, null=False)
    price = FloatField(default=0)


class ProductIngredient(DB.Model):
    ingredient_id = PrimaryKeyField()
    product_id = ForeignKeyField(Product, backref='ingredients')
    name = CharField(null=False)

    # метод для фильтрации продуктов по ингредиентам, принимает список или список из одного элемента
    # TODO: добавить игредиенты как ForeignKeyField в Product, перенести filter_products туда
    @classmethod
    def filter_products(cls, product_list):
        result = ProductIngredient.select().where(cls.name.in_(product_list))
        return result

    class Meta:
        table_name = 'product ingredients'
