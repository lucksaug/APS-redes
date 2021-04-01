from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.coonfig['SECRET_KEY'] = ''
#app.config['SQLALCHEMY_DATABASE_URI'] = ''
#db = SQLAlchemy(app)

from projeto import routes