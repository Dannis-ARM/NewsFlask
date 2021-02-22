from . import index_bp
from ... import redis_store
from flask import session


@index_bp.route('/')
def index():
    # # test redis
    # redis_store.set("name","Dannis")
    # print(redis_store.get("name"))

    # # test session
    # session["name"] = "Dannis"
    # print(session.get("name"))
    # 测试



    return "hello index"


