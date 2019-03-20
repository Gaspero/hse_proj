# -*- coding: utf-8 -*-

import random
from flask_restful import Resource, reqparse
from playhouse.shortcuts import model_to_dict

from application import DB
from models.category import Category


class AddCategory(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='Incorrect name', location='json')
        super(AddCategory, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        # with DB.atomic():
        query = Category.insert(**args)
        qraw = query.sql()
        query.execute()

        return {'isSuccess': True, 'query': qraw}


class GetCategories(Resource):

    def get(self):
        result = []
        categories = Category.select()
        for m in categories:
            result.append(model_to_dict(m))

        return {'result': result}


class DeleteCategory(Resource):

    def delete(self, category_id):
        # with DB.atomic():
        query = Category.delete().where(Category.category_id == category_id)
        query.execute()
        qraw = query.sql()

        return {'isSuccess': True, 'query': qraw}
        # TODO: добавить update
