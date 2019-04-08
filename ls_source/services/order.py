# -*- coding: utf-8 -*-

import logging
from playhouse.shortcuts import model_to_dict
from flask_restful import Resource, reqparse

from application import DB
from models.order import Order

class TestOrder(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(TestOrder, self).__init__()

    def get(self, order_id):
        result = Order.get_by_id(order_id).find_producers()
        if result:
            return {'result': model_to_dict(result.first())}  # TODO: issue - if none and we return string, throws an error
        else:
            return {'result': 'Nothing found'}


class GetOrders(Resource):
    def get(self):
        orders = []
        result = Order.select()
        for order in result:
            row = model_to_dict(order, exclude=[Order.create_time,
                                                Order.customer_id.create_time,
                                                Order.customer_id.birth_day])
            row['create_time'] = order.create_time.strftime('%Y-%m-%d %H:%M:%S')
            orders.append(row)
        return {'result': orders}
    # TODO: добавить create_time и birth_day в ответ сервера


class AddOrder(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('customer_id', type=int, required=True,
                                   help='Incorrect customer_id', location='json')
        self.reqparse.add_argument('order_status', type=str, required=True,
                                   help='Incorrect order_status', location='json')
        self.reqparse.add_argument('producer_id', type=int, required=False,
                                   help='Incorrect producer_id', location='json')
        super(AddOrder, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        filtered_args = {k: v for k, v in args.items() if v is not None}
        args.clear()
        args.update(filtered_args)
        # with DB.atomic():
        order = Order.create(**args)
        return {'isSuccess': True, 'product_id': order.order_id}
    # TODO: сделать поле producer необязательным в модели и здесь при валидации, присваивать автоматически.
    # TODO: нет обработки ошибок, когда продюсера или юзера не существует


class DeleteOrder(Resource):
    def delete(self, order_id):
        query = Order.delete().where(Order.order_id == order_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}


class UpdateOrder(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('customer_id', type=int, required=False,
                                   help='Incorrect customer_id', location='json')
        self.reqparse.add_argument('order_status', type=str, required=False,
                                   help='Incorrect order_status', location='json')
        self.reqparse.add_argument('producer_id', type=int, required=False,
                                   help='Incorrect producer_id', location='json')
        super(UpdateOrder, self).__init__()

    def put(self, order_id):
        args = self.reqparse.parse_args()
        filtered_args = {k: v for k, v in args.items() if v is not None}
        args.clear()
        args.update(filtered_args)
        query = Order.update(**args).where(Order.order_id == order_id)
        num = query.execute()
        return {'isSuccess': True, 'rowsUpdated': str(num)}
    # TODO: не обрабатывает ошибку, когда данный id не найден
