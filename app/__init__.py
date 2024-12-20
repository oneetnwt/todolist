from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
secret_key = os.getenv('SECRET_KEY')
db_uri = os.getenv('DB_URI')
db_name = os.getenv('DB_NAME')
print(secret_key)
print(db_uri)
print(db_name)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(views, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    return app

def create_db(app):
    if not os.path.exists('website/' + db_name):
        db.create_all(app=app)
        print('Database created')