from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from .config.config import Config

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .resource import resource_bp
        from .entity.user_entity import UserModel

        app.register_blueprint(resource_bp)

        @login_manager.user_loader
        def load_user(user_id):
            return UserModel.query.get(int(user_id))

        return app
