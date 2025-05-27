from config.db import db, ma
from marshmallow import fields

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.BigInteger, primary_key=True)
    receta_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)

    def __init__(self, receta_id, calificacion):
        self.receta_id = receta_id
        self.calificacion = calificacion

class RatingSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    receta_id = fields.Integer(required=True)
    calificacion = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'receta_id', 'calificacion')
        model = Rating

rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)