from config.db import app, db, ma
from marshmallow import Schema, fields

class Users(db.Model):
    __tablename__ = "tblusers"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(50))

    def __init__(self, fullname, email):
        self.fullname = fullname
        self.email = email

class UsersSchema(Schema):
    id = fields.Integer()
    fullname = fields.String()
    email = fields.String()