from datetime import datetime
from peewee import *

from application import DB


class Producer(DB.Model):

    producer_id = PrimaryKeyField()
    name = CharField(50, null=False)
    address = CharField(50, null=False)
    workers = IntegerField(100, default=0)
    working_hours = CharField(100, null=False)

    class Meta:
        table_name = 'producers'