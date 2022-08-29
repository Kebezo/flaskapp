from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hnxfwzdteurpuf:3d311ecbb5aab7f6f61eb0919ad9418a48a97321c067fce4fb0546c017957554@ec2-34-234-240-121.compute-1.amazonaws.com:5432/ddein4lv8a6lm7'
#randomly genereirano hexadecimal stevilo
app.config['SECRET_KEY'] = '52627e432fe1def0e3834e53'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = ('login_page')
login_manager.login_message_category = 'info'

from market import Routes