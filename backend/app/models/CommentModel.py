from config.db import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.BigInteger, primary_key=True)
    receta_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    contenido = db.Column(db.Text)

    def __init__(self, receta_id, contenido):
        self.receta_id = receta_id
        self.contenido = contenido

class CommentSchema(ma.Schema):
    id = fields.Integer()
    receta_id = fields.Integer()
    contenido = fields.String()

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)