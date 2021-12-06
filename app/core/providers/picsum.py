import requests
from math import ceil


class Picsum:
    def __init__(self):
        pass

    def get(self, limit):
        res = []
        page = ceil(limit / 30)
        API_URL = f"https://picsum.photos/v2/list?page={page}&limit={limit}"
        r = requests.get(API_URL).json()
        for image in r:
            image_url = image["url"]
            author = image["author"]
            res.append({"author": author, "image_url": image_url})
        return res, 200
