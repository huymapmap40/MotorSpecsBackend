from flask import Blueprint, request, jsonify
from .extensions import mongo
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     data = mongo.db.testabc.insert({'brand':'test532'})
#     return jsonify({'result':"Success!"})

@main.route('/', methods=['GET'])
def get_all_manufacturer():
    manufacturer = mongo.db.manufacturer
    output = []
    for s in manufacturer.find():
        output.append({'id': str(s['_id']),'brand': s['brand']})
    return jsonify({'result':output})
