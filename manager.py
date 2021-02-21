from datetime import timedelta

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_session import Session
from flask_wtf.csrf import CSRFProtect

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/testDB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "IQQJJASDU9199UFAJDD"

    # redis
    redis_host = "localhost"
    redis_port = 6379

    # session
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host = redis_host, port= redis_port)
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=5)

# init app
app = Flask(__name__)
app.config.from_object(Config)

# config database
db = SQLAlchemy(app)

# config redis
redis_store = StrictRedis(host = Config.redis_host, port = Config.redis_port, decode_responses= True)

# config session
sess = Session()
sess.init_app(app)

# config csrf
csrf = CSRFProtect(app)

# redis_store.set("Dannis","manager")

@app.route('/')
def hello_world():
    # session["name"] = "Dannis"
    # print(session.get("name"))
    return "hello world"

if __name__ == "__main__":
    app.run()