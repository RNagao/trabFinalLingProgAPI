from flask import Flask
from .extensions import db, migrate, ma
from .config import Config

from .questoes.routes import questoes_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(questoes_api)

    return app