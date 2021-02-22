from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_wtf.csrf import CSRFProtect


from config import config_dict

# create redis instance
redis_store = None
# create database instance
db = SQLAlchemy()

def create_app(config_name):

    # set config env
    Config = config_dict.get(config_name)

    # call log_file()
    register_log(Config.LEVEL_NAME)

    # init app
    app = Flask(__name__)
    app.config.from_object(Config)

    # config database
    db.init_app(app)

    # config redis
    global redis_store
    redis_store = StrictRedis(host=Config.redis_host, port=Config.redis_port, decode_responses=True)

    # config session
    sess = Session()
    sess.init_app(app)

    # config csrf
    csrf = CSRFProtect(app)

    # register bluepints
    from App.modules.index import index_bp
    app.register_blueprint(index_bp)
    # print(app.url_map)

    return app

import logging
from logging.handlers import RotatingFileHandler

def register_log(LEVEL_NAME):
    # 设置日志的记录等级,常见的有四种,大小关系如下: DEBUG < INFO < WARNING < ERROR
    logging.basicConfig(level=LEVEL_NAME)  # 调试debug级,一旦设置级别那么大于等于该级别的信息全部都会输出
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)