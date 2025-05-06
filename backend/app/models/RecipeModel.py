from config.db import db, ma
from marshmallow import fields
from datetime import datetime

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.BigInteger, primary_key=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    ingredientes = db.Column(db.Text)
    preparacion = db.Column(db.Text)
    categoria_id = db.Column(db.BigInteger, db.ForeignKey('categories.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    promedio_calificacion = db.Column(db.Float, nullable=True, default=None)

    def __init__(self, usuario_id, titulo, descripcion, ingredientes, preparacion, categoria_id, fecha_creacion=None):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.ingredientes = ingredientes
        self.preparacion = preparacion
        self.categoria_id = categoria_id
        self.fecha_creacion = fecha_creacion or datetime.utcnow()

class RecipeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    usuario_id = fields.Integer(required=True)
    titulo = fields.String(required=True)
    descripcion = fields.String()
    ingredientes = fields.String()
    preparacion = fields.String()
    categoria_id = fields.Integer(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
    promedio_calificacion = fields.Float(dump_only=True)

    class Meta:
        fields = ('id', 'usuario_id', 'titulo', 'descripcion', 'ingredientes', 'preparacion', 'categoria_id', 'fecha_creacion', 'promedio_calificacion')
        model = Recipe

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)