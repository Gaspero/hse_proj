# -*- coding: utf-8 -*-

import logging
from playhouse.shortcuts import model_to_dict
from flask_restful import Resource, reqparse
from flask import jsonify

from application import DB
from models.order import Order, OrderItem


class GetOrderItems(Resource):
    def get(self, order_id):
        result = OrderItem.select().where(OrderItem.order_id == order_id)
        order_items = []
        for order_item in result:
            row = model_to_dict(order_item, exclude=[OrderItem.order_id, OrderItem.product_id.create_time])
            order_items.append(row)
        return {'result': order_items}
    # TODO: что будет, когда пусто?


class AddOrderItem(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('product_id', type=int, required=True,
                                   help='Incorrect product_id', location='json')
        self.reqparse.add_argument('quantity', type=int, required=True,
                                   help='Incorrect quantity', location='json')
        super(AddOrderItem, self).__init__()

    def post(self, order_id):
        args = self.reqparse.parse_args()
        # with DB.atomic():
        order_item = OrderItem.create(**args, order_id=order_id)
        return {'isSuccess': True, 'product_id': order_item.item_id}
    # TODO: нет обработки ошибок, когда продука или заказа не существует


class DeleteOrderItem(Resource):
    def delete(self, order_id, item_id):
        query = OrderItem.delete().where(OrderItem.item_id == item_id, OrderItem.order_id == order_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}


class UpdateOrderItem(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('product_id', type=int, required=False,
                                   help='Incorrect product_id', location='json')
        self.reqparse.add_argument('quantity', type=int, required=False,
                                   help='Incorrect quantity', location='json')
        super(UpdateOrderItem, self).__init__()

    def put(self, order_id, item_id):
        args = self.reqparse.parse_args()
        filtered_args = {k: v for k, v in args.items() if v is not None}
        args.clear()
        args.update(filtered_args)
        query = OrderItem.update(**args).where(OrderItem.item_id == item_id, OrderItem.order_id == order_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}
