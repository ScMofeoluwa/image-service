import requests
from .. import cache
from ..utils import api_key_required
from flask_restful import Resource


class Woof(Resource):
    @api_key_required
    @cache.cached(timeout=30, query_string=True)
    def get(self):
        API_URL = "https://random.dog/woof.json"
        r = requests.get(API_URL)
        image_url = r.json()["url"]
        return {"image_name": "dog", "image_url": image_url}, 200
