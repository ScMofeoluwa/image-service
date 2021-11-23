import requests
from math import ceil
from .. import cache
from ..utils import api_key_required
from flask_restful import Resource


class Foodish(Resource):
    @api_key_required
    @cache.cached()
    def get(self, amount):
        API_URL = "https://foodish-api.herokuapp.com/api/"
        res = []
        for i in range(amount):
            r = requests.get(API_URL).json()
            image_name = r["image"].split("/")[-2]
            image_url = r["image"]
            res.append({"image_name": image_name, "image_url": image_url})
        return res, 200
