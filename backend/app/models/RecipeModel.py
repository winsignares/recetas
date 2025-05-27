from config.db import db, ma
from marshmallow import fields
from datetime import datetime

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.BigInteger, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    ingredientes = db.Column(db.Text)
    preparacion = db.Column(db.Text)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    promedio_calificacion = db.Column(db.Float, nullable=True, default=None)

    comentarios = db.relationship('Comment', backref='receta', lazy=True, cascade='all, delete-orphan')
    calificaciones = db.relationship('Rating', backref='receta', lazy=True, cascade='all, delete-orphan')
    imagenes = db.relationship('RecipeImage', backref='receta', lazy=True, cascade='all, delete-orphan')

    def __init__(self, titulo, descripcion, ingredientes, preparacion, fecha_creacion=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.ingredientes = ingredientes
        self.preparacion = preparacion
        self.fecha_creacion = fecha_creacion or datetime.utcnow()


class RecipeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    titulo = fields.String(required=True)
    descripcion = fields.String()
    ingredientes = fields.String()
    preparacion = fields.String()
    fecha_creacion = fields.DateTime(dump_only=True)
    promedio_calificacion = fields.Float(dump_only=True)

    # Relaciones serializadas
    comentarios = fields.Nested('CommentSchema', many=True)
    calificaciones = fields.Nested('RatingSchema', many=True)
    imagenes = fields.Nested('RecipeImageSchema', many=True)

    class Meta:
        fields = (
            'id',
            'titulo',
            'descripcion',
            'ingredientes',
            'preparacion',
            'fecha_creacion',
            'promedio_calificacion',
            'comentarios',
            'calificaciones',
            'imagenes'
        )
        model = Recipe

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)
