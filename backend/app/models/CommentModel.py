from config.db import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.BigInteger, primary_key=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    receta_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    contenido = db.Column(db.Text)

    def __init__(self, usuario_id, receta_id, contenido):
        self.usuario_id = usuario_id
        self.receta_id = receta_id
        self.contenido = contenido

class CommentSchema(ma.Schema):
    id = fields.Integer()
    usuario_id = fields.Integer()
    receta_id = fields.Integer()
    contenido = fields.String()

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)