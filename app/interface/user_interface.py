from ..entity.user_entity import UserModel
from .. import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        load_only = ('password',)
