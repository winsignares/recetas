from config.db import db, ma
from marshmallow import fields

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.BigInteger, primary_key=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    titulo = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    ingredientes = db.Column(db.Text)
    preparacion = db.Column(db.Text)
    categoria_id = db.Column(db.BigInteger, db.ForeignKey('categories.id'))
    fecha_creacion = db.Column(db.DateTime)
    promedio_calificacion = db.Column(db.Float)

    def __init__(self, usuario_id, titulo, descripcion, ingredientes, preparacion, categoria_id, fecha_creacion, promedio_calificacion=None):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.ingredientes = ingredientes
        self.preparacion = preparacion
        self.categoria_id = categoria_id
        self.fecha_creacion = fecha_creacion
        self.promedio_calificacion = promedio_calificacion

class RecipeSchema(ma.Schema):
    id = fields.Integer()
    usuario_id = fields.Integer()
    titulo = fields.String()
    descripcion = fields.String()
    ingredientes = fields.String()
    preparacion = fields.String()
    categoria_id = fields.Integer(allow_none=True)
    fecha_creacion = fields.DateTime()
    promedio_calificacion = fields.Float(allow_none=True)

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)