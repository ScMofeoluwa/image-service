from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from ..usecase.user_usecase import UserUsecase
from ..interface.user_interface import UserSchema
user_schema = UserSchema()


class UserRegister(Resource):
    def post(self):
        try:
            user = user_schema.load(request.get_json())
            print('load')
        except ValidationError as err:
            return err.messages, 400

        user.password = user.generate_hash(user.password)
        UserUsecase.register(user)

        return {"message": "user created successfully"}, 201
