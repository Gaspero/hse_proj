# -*- coding: utf-8 -*-


from flask_peewee.rest import Authentication


def init_api(api):
    from models.category import Category
    from models.customer import Customer
    from models.order import Order, OrderItem
    from models.product import Product, ProductIngredient

    api.default_auth = Authentication(protected_methods=[])
    api.register(Category)
    api.register(Product)
    api.register(ProductIngredient)
    api.register(Customer)
    api.register(Order)
    api.register(OrderItem)

    api.setup()
