# -*- coding: utf-8 -*-


def init_models(db):

    from models.category import Category
    from models.customer import Customer
    from models.order import Order, OrderItem
    from models.product import Product, ProductAdditional, ProductIngredient
    from models.producers import Producer

    ms = [Product, Customer, Order, OrderItem, Producer, ProductAdditional, ProductIngredient, Category]

    db.database.create_tables(ms)
