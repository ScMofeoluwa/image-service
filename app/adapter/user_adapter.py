from flask import request
from marshmallow import ValidationError
from ..usecase.user_usecase import UserUsecase
from ..interface.user_interface import UserSchema
user_schema = UserSchema()


class UserAdapter:
    def __init__(self, usecase: UserUsecase, schema=UserSchema):
        self.usecase = usecase
        self.schema = schema

    @staticmethod
    def add_user():
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        user.password = user.generate_hash(user.password)
        return UserUsecase.register(user)
