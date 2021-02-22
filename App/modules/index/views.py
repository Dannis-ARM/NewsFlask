import logging

from . import index_bp
from ... import redis_store
from flask import session, current_app


@index_bp.route('/')
def index():
    # # test redis
    # redis_store.set("name","Dannis")
    # print(redis_store.get("name"))

    # # test session
    # session["name"] = "Dannis"
    # print(session.get("name"))
    # 测试

    logging.error("yes")
    current_app.logger.info('info log')
    current_app.logger.debug('debug log')
    current_app.logger.warning('warning log')
    current_app.logger.error('error log')

    return "hello index"


