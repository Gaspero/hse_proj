# -*- coding: utf-8 -*-

from application import DB
from models.customer import Customer
from models.producers import Producer

def matcher(cust):
    for producer in Producer.select().where(Producer.district == cust.district):  # TODO: добавить проверку на раб часы
        return(producer)  # TODO: заменить на Yield и добавить выбор первого
