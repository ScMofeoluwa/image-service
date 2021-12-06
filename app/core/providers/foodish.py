import requests


class Foodish:
    def __init__(self):
        pass

    def get(self, limit):
        API_URL = "https://foodish-api.herokuapp.com/api/"
        res = []
        for i in range(limit):
            r = requests.get(API_URL).json()
            image_name = r["image"].split("/")[-2]
            image_url = r["image"]
            res.append({"image_name": image_name, "image_url": image_url})
        return res, 200
