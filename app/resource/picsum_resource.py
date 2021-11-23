import requests
from math import ceil
from .. import cache
from ..utils import api_key_required
from flask_restful import Resource


class Picsum(Resource):
    @api_key_required
    @cache.cached()
    def get(self, amount):
        res = []
        page = ceil(amount / 30)
        API_URL = f"https://picsum.photos/v2/list?page={page}&limit={amount}"
        r = requests.get(API_URL).json()
        for image in r:
            image_url = image["url"]
            author = image["author"]
            res.append({"author": author, "image_url": image_url})
        return res, 200
