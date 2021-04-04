from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8ba8d1387bcb2460b0a5cc0831c0db65'
#app.config['SQLALCHEMY_DATABASE_URI'] = ''
#db = SQLAlchemy(app)

from projeto import routes