# -*- coding: utf-8 -*-

import random
from playhouse.shortcuts import model_to_dict
from flask_restful import Resource, reqparse
import logging
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
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='Incorrect name', location='json')
        self.reqparse.add_argument('price', type=float, required=True,
                                   help='Incorrect last_name', location='json')
        self.reqparse.add_argument('description', type=str, required=True,
                                   help='Incorrect description', location='json')
        self.reqparse.add_argument('size', type=str, required=True,
                                   help='Incorrect size', location='json')
        super(AddProduct, self).__init__()

    def post(self, category_id):
        args = self.reqparse.parse_args()
        # with DB.atomic():
        product = Product.create(**args, category_id=category_id)
        return {'isSuccess': True, 'product_id': product.product_id}


class DeleteProduct(Resource):

    def delete(self, product_id):
        query = Product.delete().where(Product.product_id == product_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}


class UpdateProduct(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=False,
                                   help='Incorrect name', location='json')
        self.reqparse.add_argument('price', type=float, required=False,
                                   help='Incorrect last_name', location='json')
        self.reqparse.add_argument('description', type=str, required=False,
                                   help='Incorrect description', location='json')
        self.reqparse.add_argument('size', type=str, required=False,
                                   help='Incorrect size', location='json')
        super(UpdateProduct, self).__init__()

    def put(self, product_id):
        args = self.reqparse.parse_args()
        filtered_args = {k: v for k, v in args.items() if v is not None}
        args.clear()
        args.update(filtered_args)
        query = Product.update(**args).where(Product.product_id == product_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}
    # TODO: не обрабатывает ошибку, когда данный id не найден

