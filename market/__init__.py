from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kutycmqskxrzpc:0a53ecba63f91bc9ac1854054114c3522ac6f81115ca841f9e506b7b12538100@ec2-34-234-240-121.compute-1.amazonaws.com:5432/dbbos429tdhhb8'
#randomly genereirano hexadecimal stevilo
app.config['SECRET_KEY'] = '52627e432fe1def0e3834e53'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = ('login_page')
login_manager.login_message_category = 'info'

from market import Routes