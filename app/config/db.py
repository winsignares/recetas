from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

user = "root"
password= "root"
nombrecontainer= "mysql_container"
namebd = "recetas_db"

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{nombrecontainer}/{namebd}'
app.congig['SQLALCHEMY_TRACK:NOTIFICATIONS'] = False
app.secret_key = "ingweb"

db = SQLAlchemy(app)
ma = Marshmallow(app)