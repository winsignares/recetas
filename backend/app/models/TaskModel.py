from config.db import app, db, ma
from marshmallow import Schema, fields

class Task(db.Model):
    __tablename__ = "tbltask"

    id = db.Column(db.Integer, primary_key = True)
    nametask = db.Column(db.String(50))
    id_user_fk = db.Column(db.Integer, db.ForeignKey('tblusers.id'))
    id_category_fk = db.Column(db.Integer, db.ForeignKey('tblcategory.id'))

    def __init__(self, nametask, id_user_fk, id_category_fk):
        self.nametask = nametask
        self.id_user_fk = id_user_fk
        self.id_category_fk = id_category_fk


class TaskSchema(Schema):
    class Meta:
        id = fields.Integer()
        nametask = fields.String()
        id_user_fk = fields.Integer()
        id_category_fk = fields.Integer()
