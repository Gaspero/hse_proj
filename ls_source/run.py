# -*- coding: utf-8 -*-

import os
import logging
from datetime import datetime
from shutil import copyfile


def make_loggers():
    formatter = logging.Formatter('%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s')
    logger = logging.getLogger()

    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


if __name__ == '__main__':

    log = make_loggers()

    if not os.path.isfile('local_settings.py.tmpl'):
        log.error('Отсутствует шаблон локального файла настроек.')

    else:

        try:
            import local_settings
        except ImportError:
            copyfile('local_settings.py.tmpl', 'local_settings.py')
            log.warning('Отсутствует локальный файл настроек. Файл создан из шаблона local_settings.py.tmpl')

        try:
            log.debug('Launched: application %s' % datetime.now())
            from application import APP
            APP.run()
        except Exception as e:
            log.exception(e)
