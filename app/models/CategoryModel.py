from config.db import app, db, ma
from marshmallow import Schema, fields

class Category(db.Model):
    __tablename__ = "tblcategory"

    id = db.Column(db.Integer, primary_key = True)
    namecategory = db.Column(db.String(50))

    def __init__(self, namecategory):
        self.namecategory = namecategory


with app.app_context():
    db.create_all()


class CategorySchema(Schema):
    class Meta:
        id = fields.Integer()
        namecategory = fields.String()