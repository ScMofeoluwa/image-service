from flask import request
from functools import wraps
from app.entity.user_entity import UserModel


def api_key_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        exists = UserModel.query.filter_by(api_key=api_key).first()
        if not exists:
            return {
                "description": "Request does not contain an api key.",
                "error": "authorization_required",
            }, 401
        return f(*args, **kwargs)

    return wrapper
