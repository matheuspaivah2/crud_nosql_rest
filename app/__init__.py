from flask import Flask

from app import views
from environs import Env

env = Env()
env.read_env()

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]

def create_app():
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False

    views.init_app(app)

    return app