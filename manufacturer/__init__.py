from flask import Flask
from .extensions import mongo
from .main import main
# from mongoengine_jsonencoder import MongoEngineJSONEncoder

def create_app(config_object='manufacturer.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)
    app.register_blueprint(main)
    return app