from flask import Flask
from dotenv import load_dotenv
import os

secret_key = os.getenv('SECRET_KEY')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(views, url_prefix='/')

    return app