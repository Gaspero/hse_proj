# -*- coding: utf-8 -*-

# Файл с локальными конфигами проекта

from settings import *


DB_ENGINE = 'peewee.SqliteDatabase'  # раскомментировать если необходимо работать с SQLite


DATABASE = {'engine': DB_ENGINE, 'name':'testing.db'}
"""
            'name': 'XXXXXX', 'user': 'XXXXXX',  # name (имя БД) и user необходимо указать свои
            'password': 'XXXXXX',  # password необходимо указать свой
            'host': 'team2018.piterdata.ninja', 'port': 5432}
"""
