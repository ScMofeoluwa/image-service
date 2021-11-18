from flask import request
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required
from marshmallow import ValidationError
from ..usecase.user_usecase import UserUsecase
from ..interface.user_interface import UserSchema
user_schema = UserSchema()


class UserRegister(Resource):
    def post(self):
        try:
            user_json = request.get_json()
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if UserUsecase.find_by_username(user_json['username']):
            return {"message": "user with username already exists"}, 400

        user.password = user.generate_hash(user.password)
        user.api_key = user.generate_api_key()
        UserUsecase.register(user)

        return {"message": "user created successfully"}, 201


class UserLogin(Resource):
    def post(self):
        try:
            user_json = request.get_json()
        except ValidationError as err:
            return err.messages, 400

        user = UserUsecase.find_by_username(user_json["username"])

        if user and user.verify_hash(user.password, user_json["password"]):
            login_user(user)
            return {"api_key": user.api_key}, 200

        return {"message": "Invalid credentials!"}, 401


class UserLogout(Resource):
    @login_required
    def post(self):
        logout_user()
        return {"message": "logged out"}, 200
