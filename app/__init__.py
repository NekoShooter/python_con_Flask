from flask import Flask, url_for
from flask_login import LoginManager
from .configuracion import produccion
from .autenticacion import autenticacion

login_manager = LoginManager()
login_manager.login_view = 'autenticacion.logearse'
login_manager.login_message = 'por favor logeate'


def crearAPP() -> object:
    app = Flask(__name__)
    app.config.from_object(produccion)
    app.register_blueprint(autenticacion) # registrar el blue print
    login_manager.init_app(app)
    return app
