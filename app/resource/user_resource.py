from ..adapter.user_adapter import UserAdapter
from flask_restful import Resource


class UserRegister(Resource):
    def __init__(self, adapter=UserAdapter):
        self.adapter = adapter

    def post(self):
        self.adapter.add_user()

        return {"message": "user created successfully"}, 201
