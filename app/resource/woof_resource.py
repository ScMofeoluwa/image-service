import requests
from ..utils import api_key_required
from flask_restful import Resource


class Woof(Resource):
    @api_key_required
    def get(self):
        res = requests.get('https://random.dog/woof.json')
        url = res.json()['url']
        return {"image_name": "dog", "image_url": url}, 200
