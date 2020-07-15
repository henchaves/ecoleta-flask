from flask_restful import Resource, reqparse
from ecoleta.ext.api.models.spot import SpotModel




class SpotList(Resource):
    def get(self):
        return {"spots": [spot.json() for spot in SpotModel.find_all()]}, 200

class Spot(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("uf", type=str, required=True, help="This field cannot be left blank.")
    parser.add_argument("city", type=str, required=True, help="This field cannot be left blank.")
    parser.add_argument("categories", type=str, required=True, help="This field cannot be left blank.")

    def get(self, name):
        spot = SpotModel.find_by_name(name)
        if not spot:
            return {"message": "Spot not found."}, 404
        return spot.json(), 200
    
    def post(self, name):
        if SpotModel.find_by_name(name):
            return {"message": f"A spot with name '{name}' already exists."}, 400
        data = Spot.parser.parse_args()
        spot = SpotModel(name, **data)
        try:
            spot.save_spot()
        except:
            return {"message": "An internal error ocurred while saving the spot."}, 500
        return spot.json(), 201

    def put(self, name):
        pass

    def delete(self, name):
        pass