import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_wtf.csrf import CSRFProtect

from config import config_dict
redis_store = None

def create_app(config_name):
    # set config env
    Config = config_dict.get(config_name)

    # call log_file()
    register_log(Config.LEVEL_NAME)

    # init app
    app = Flask(__name__)
    app.config.from_object(Config)

    # config database
    db = SQLAlchemy(app)

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

def register_log(LEVEL_NAME):
    # 默认日志等级的设置
    logging.basicConfig(level=LEVEL_NAME)
    # 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
    file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024 * 1024, backupCount=10)
    # 设置日志的格式                   发生时间    日志等级     日志信息文件名      函数名          行数        日志信息
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    # 将日志记录器指定日志的格式
    file_log_handler.setFormatter(formatter)
    # 日志等级的设置
    # file_log_handler.setLevel(logging.WARNING)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)