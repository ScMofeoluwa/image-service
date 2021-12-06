import requests


class Woof:
    def __init__(self):
        pass

    def get(self, limit):
        API_URL = "https://random.dog/woof.json"
        res = []
        for i in range(limit):
            r = requests.get(API_URL).json()
            image_url = r["url"]
            res.append({"image_name": "dog", "image_url": image_url})
        return res, 200
