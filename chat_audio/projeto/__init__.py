from flask import Flask
#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Instância dos objetos
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Configurações para os objetos
app.config['SECRET_KEY'] = '8ba8d1387bcb2460b0a5cc0831c0db65'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
#app.config['MYSQL_DB']= ''
#app.config['MYSQL_CURSOR']= 'Disct'

#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_menager.login_message_category = 'info'

from projeto import routes