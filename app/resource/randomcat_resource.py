import requests
from .. import cache
from ..utils import api_key_required
from flask_restful import Resource


class RandomCat(Resource):
    @api_key_required
    @cache.cached()
    def get(self, amount):
        API_URL = "http://aws.random.cat/meow"
        res = []
        for i in range(amount):
            r = requests.get(API_URL).json()
            image_url = r["file"]
            res.append({"image_name": "cat", "image_url": image_url})
        return res, 200
