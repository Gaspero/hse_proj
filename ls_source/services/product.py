# -*- coding: utf-8 -*-

import random
from playhouse.shortcuts import model_to_dict
from flask_restful import Resource

from application import DB
from models.product import Product


class GetProducts(Resource):

    def get(self):
        products = []
        result = Product.select()
        for product in result:
            row = model_to_dict(product, exclude=[Product.create_time])
            row['create_time'] = product.create_time.strftime('%Y-%m-%d %H:%M:%S')
            products.append(row)
        return {'result': products}


class AddProduct(Resource):

    def get(self, category_id):
        with DB.atomic():
            product = Product.create(
                name='product 1 + %s' % random.random(),
                price='5',
                category_id=category_id)
        return {'isSuccess': True, 'product_id': product.product_id}


class DeleteProduct(Resource):

    def get(self, product_id):
        query = Product.delete().where(Product.product_id == product_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}


class UpdateProduct(Resource):

    def get(self, product_id):
        query = Product.update(price=10).where(Product.product_id == product_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}

