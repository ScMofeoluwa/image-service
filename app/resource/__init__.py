from flask_restful import Api
from flask import Blueprint
from ..resource.user_resource import UserRegister, UserLogin, UserLogout
from ..resource.image_resource import Image

resource_bp = Blueprint("resource", __name__)
api = Api(resource_bp, prefix="/api/v1")

api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogout, "/logout")
api.add_resource(Image, "/<string:name>/<int:limit>")
