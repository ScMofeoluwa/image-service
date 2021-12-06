import requests


class Randomfox:
    def __init__(self):
        pass

    def get(self, limit):
        API_URL = "https://randomfox.ca/floof/"
        res = []
        for i in range(limit):
            r = requests.get(API_URL).json()
            image_url = r["image"]
            res.append({"image_name": "fox", "image_url": image_url})
        return res, 200
