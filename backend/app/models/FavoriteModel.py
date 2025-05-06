from config.db import db, ma
from marshmallow import fields

class Favorite(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.BigInteger, primary_key=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    receta_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)

    def __init__(self, usuario_id, receta_id):
        self.usuario_id = usuario_id
        self.receta_id = receta_id

class FavoriteSchema(ma.Schema):
    id = fields.Integer()
    usuario_id = fields.Integer()
    receta_id = fields.Integer()

favorite_schema = FavoriteSchema()
favorites_schema = FavoriteSchema(many=True)