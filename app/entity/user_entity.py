from .. import db, bcrypt


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120))
    api_key = db.Column(db.String)

    @staticmethod
    def generate_hash(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def verify_hash(hash_pwd, password):
        return bcrypt.check_password_hash(hash_pwd, password)
