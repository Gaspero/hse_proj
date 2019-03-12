# -*- coding: utf-8 -*-

import random
from flask_restful import Resource
from playhouse.shortcuts import model_to_dict

from application import DB
from models.category import Category


class AddCategory(Resource):

    def get(self, category_name):
        name = 'Category %s - %s' % (category_name, random.random())
        with DB.atomic():
            query = Category.insert(name=name)
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
