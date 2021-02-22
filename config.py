import logging
from datetime import timedelta
from redis import StrictRedis

class Config:
    # database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/testDB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # secret_key
    SECRET_KEY = "IQQJJASDU9199UFAJDD"

    # redis
    redis_host = "localhost"
    redis_port = 6379

    # session
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host = redis_host, port= redis_port)
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=5)

    # log mode
    LEVEL_NAME = None

class DevelopConfig(Config):
    LEVEL_NAME = logging.DEBUG
    pass

class ProductConfig(Config):
    LEVEL_NAME = logging.ERROR
    pass

class TestConfig(Config):
    pass

config_dict = {
    "develop": DevelopConfig,
    "product": ProductConfig,
    "test": TestConfig
}