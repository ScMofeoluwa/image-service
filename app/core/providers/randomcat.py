import requests


class Randomcat:
    def __init__(self):
        pass

    def get(self, limit):
        API_URL = "http://aws.random.cat/meow"
        res = []
        for i in range(limit):
            r = requests.get(API_URL).json()
            image_url = r["file"]
            res.append({"image_name": "cat", "image_url": image_url})
        return res, 200
