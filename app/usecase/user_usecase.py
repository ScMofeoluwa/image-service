from ..entity.user_entity import UserModel
from .. import db


class UserUsecase:
    def __init__(self, entity: UserModel):
        self.entity = entity

    @staticmethod
    def register(data):
        db.session.add(data)
        db.session.commit()

    def find_by_id(self, _id):
        return self.entity.query.filter_by(id=_id).first()

    def find_by_username(self, username):
        return self.entity.query.filter_by(username=username).first()
