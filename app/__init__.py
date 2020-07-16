import os
from flask import Flask
from flask_ipinfo import IPInfo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['DB_MASTER'] = os.getcwd() + '/flaskcounter.db'
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///flaskcounter.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://theis:salupa@localhost/flaskcounter'
app.secret_key = os.urandom(24)
ipinfo = IPInfo()
db = SQLAlchemy(app)

conn = cursor = None



from app import routes