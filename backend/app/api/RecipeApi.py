from flask import Blueprint, request, jsonify
from config.db import db
from models.RecipeModel import Recipe, recipe_schema, recipes_schema
from datetime import datetime

recipe_routes = Blueprint('recipe_routes', __name__)

@recipe_routes.route('/', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify({"data": recipes_schema.dump(recipes)})

@recipe_routes.route('/save', methods=['POST'])
def save_recipe():
    data = request.json
    required_fields = ['usuario_id', 'titulo', 'descripcion', 'ingredientes', 'preparacion']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    new_recipe = Recipe(
        usuario_id=data['usuario_id'],
        titulo=data['titulo'],
        descripcion=data['descripcion'],
        ingredientes=data['ingredientes'],
        preparacion=data['preparacion'],
        categoria_id=data.get('categoria_id'),
        fecha_creacion=datetime.utcnow(),
        promedio_calificacion=data.get('promedio_calificacion')
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"message": "Receta guardada", "data": recipe_schema.dump(new_recipe)}), 201

@recipe_routes.route('/update', methods=['PUT'])
def update_recipe():
    id = request.json.get('id')
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    data = request.json
    recipe.titulo = data.get('titulo', recipe.titulo)
    recipe.descripcion = data.get('descripcion', recipe.descripcion)
    recipe.ingredientes = data.get('ingredientes', recipe.ingredientes)
    recipe.preparacion = data.get('preparacion', recipe.preparacion)
    recipe.categoria_id = data.get('categoria_id', recipe.categoria_id)
    recipe.promedio_calificacion = data.get('promedio_calificacion', recipe.promedio_calificacion)
    db.session.commit()
    return jsonify({"message": "Receta actualizada", "data": recipe_schema.dump(recipe)})

@recipe_routes.route('/delete/<id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Receta eliminada"})