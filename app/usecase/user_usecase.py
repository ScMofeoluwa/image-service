from ..entity.user_entity import UserModel
from .. import db


class UserUsecase:
    @staticmethod
    def register(data):
        db.session.add(data)
        db.session.commit()

    @staticmethod
    def find_by_id(_id):
        return UserModel.query.filter_by(id=_id).first()

    @staticmethod
    def find_by_username(username):
        return UserModel.query.filter_by(username=username).first()
