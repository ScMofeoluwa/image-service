import requests
from .. import cache
from ..utils import api_key_required
from flask_restful import Resource


class Woof(Resource):
    @api_key_required
    @cache.cached()
    def get(self, amount):
        API_URL = "https://random.dog/woof.json"
        res = []
        for i in range(amount):
            r = requests.get(API_URL)
            image_url = r.json()["url"]
            res.append({"image_name": "dog", "image_url": image_url})
        return res, 200
