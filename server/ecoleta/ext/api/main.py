from flask import Blueprint
from flask_restful import Api

from .resources.spot import SpotList, Spot

bp = Blueprint("api", __name__)
api = Api(bp)

api.add_resource(SpotList, "/spots")
api.add_resource(Spot, "/spot/<string:name>")