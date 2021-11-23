import requests
from .. import cache
from ..utils import api_key_required
from flask_restful import Resource


class RandomFox(Resource):
    @api_key_required
    @cache.cached()
    def get(self, amount):
        API_URL = "https://randomfox.ca/floof/"
        res = []
        for i in range(amount):
            r = requests.get(API_URL).json()
            image_url = r["image"]
            res.append({"image_name": "fox", "image_url": image_url})
        return res, 200
