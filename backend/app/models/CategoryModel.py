from config.db import db, ma
from marshmallow import fields

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.BigInteger, primary_key=True)
    nombre = db.Column(db.String(255))

    def __init__(self, nombre):
        self.nombre = nombre

class CategorySchema(ma.Schema):
    id = fields.Integer()
    nombre = fields.String()

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)