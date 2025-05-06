from flask import Blueprint, request, jsonify
from config.db import db
from models.RecipeModel import Recipe, recipe_schema, recipes_schema
from models.UsersModel import User
from models.CategoryModel import Category

recipe_routes = Blueprint('recipe_routes', __name__)

@recipe_routes.route('/', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify({"data": recipes_schema.dump(recipes)})

@recipe_routes.route('/save', methods=['POST'])
def save_recipe():
    data = request.get_json()
    usuario_id = data.get('usuario_id')
    titulo = data.get('titulo')
    descripcion = data.get('descripcion')
    ingredientes = data.get('ingredientes')
    preparacion = data.get('preparacion')
    categoria_id = data.get('categoria_id')

    if not all([usuario_id, titulo, categoria_id]):
        return jsonify({"error": "Faltan datos requeridos: usuario_id, titulo o categoria_id"}), 400

    if not User.query.get(usuario_id):
        return jsonify({"error": "Usuario no encontrado"}), 404
    if not Category.query.get(categoria_id):
        return jsonify({"error": "Categoría no encontrada"}), 404

    new_recipe = Recipe(
        usuario_id=usuario_id,
        titulo=titulo,
        descripcion=descripcion,
        ingredientes=ingredientes,
        preparacion=preparacion,
        categoria_id=categoria_id
    )
    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({"message": "Receta guardada", "data": recipe_schema.dump(new_recipe)}), 201

@recipe_routes.route('/update', methods=['PUT'])
def update_recipe():
    data = request.get_json()
    id = data.get('id')
    usuario_id = data.get('usuario_id')
    titulo = data.get('titulo')
    descripcion = data.get('descripcion')
    ingredientes = data.get('ingredientes')
    preparacion = data.get('preparacion')
    categoria_id = data.get('categoria_id')

    if not id:
        return jsonify({"error": "Falta el campo id"}), 400

    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    if usuario_id and not User.query.get(usuario_id):
        return jsonify({"error": "Usuario no encontrado"}), 404
    if categoria_id and not Category.query.get(categoria_id):
        return jsonify({"error": "Categoría no encontrada"}), 404

    if usuario_id:
        recipe.usuario_id = usuario_id
    if titulo:
        recipe.titulo = titulo
    if descripcion is not None:
        recipe.descripcion = descripcion
    if ingredientes is not None:
        recipe.ingredientes = ingredientes
    if preparacion is not None:
        recipe.preparacion = preparacion
    if categoria_id:
        recipe.categoria_id = categoria_id

    db.session.commit()
    return jsonify({"message": "Receta actualizada", "data": recipe_schema.dump(recipe)}), 200

@recipe_routes.route('/delete/<id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Receta eliminada"}), 200