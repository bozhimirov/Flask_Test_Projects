import os

from flask import Flask
from flaskblog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__, instance_relative_config=True)
# app.config.from_mapping(
#     SECRET_KEY='dev',
#     MAIL_USERNAME='dev',
#     MAIL_PASSWORD='dev',
# )
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config.from_object(Config)
db = SQLAlchemy(app)
# db.init_app(app)
# migrate = Migrate(app)
# migrate.init_app(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
mail = Mail(app)

from flaskblog import routes, models
