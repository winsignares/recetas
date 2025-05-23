from config.db import db, ma
from marshmallow import fields

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.BigInteger, primary_key=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    receta_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)

    def __init__(self, usuario_id, receta_id, calificacion):
        self.usuario_id = usuario_id
        self.receta_id = receta_id
        self.calificacion = calificacion

class RatingSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    usuario_id = fields.Integer(required=True)
    receta_id = fields.Integer(required=True)
    calificacion = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'usuario_id', 'receta_id', 'calificacion')
        model = Rating

rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)