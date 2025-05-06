from config.db import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    nombre = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    contraseña = db.Column(db.String(255))
    fecha_registro = db.Column(db.DateTime)

    def __init__(self, nombre, email, contraseña, fecha_registro):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro

class UserSchema(ma.Schema):
    id = fields.Integer()
    nombre = fields.String()
    email = fields.String()
    fecha_registro = fields.DateTime()

user_schema = UserSchema()
users_schema = UserSchema(many=True)