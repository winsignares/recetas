from flask import Blueprint, request, jsonify
from config.db import db
from models.RecipeModel import Recipe, recipe_schema, recipes_schema
from models.UsersModel import User
from models.RecipeImageModel import RecipeImage
from werkzeug.utils import secure_filename
from .RecipeImageApi import allowed_file

recipe_routes = Blueprint('recipe_routes', __name__)

@recipe_routes.route('/', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify({"data": recipes_schema.dump(recipes)})


@recipe_routes.route('/<int:id>', methods=['GET'])
def get_recipe_by_id(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    return jsonify({"data": recipe_schema.dump(recipe)}), 200


@recipe_routes.route('/save_with_image', methods=['POST'])
def save_recipe_with_image():
    if 'titulo' not in request.form or 'image' not in request.files:
        return jsonify({"error": "Faltan datos requeridos: titulo o image"}), 400

    # Obtener datos de la receta
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    ingredientes = request.form.get('ingredientes')
    preparacion = request.form.get('preparacion')

    if not titulo:
        return jsonify({"error": "Faltan datos requeridos: titulo"}), 400

    # Crear la receta
    new_recipe = Recipe(
        titulo=titulo,
        descripcion=descripcion,
        ingredientes=ingredientes,
        preparacion=preparacion
    )
    db.session.add(new_recipe)
    db.session.flush()  # Obtener el ID de la receta antes de commit

    # Manejar la imagen
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó ningún archivo"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Formato de archivo no permitido"}), 400

    filename = secure_filename(file.filename)
    file_type = file.mimetype
    image_data = file.read()

    new_image = RecipeImage(
        receta_id=new_recipe.id,
        download_url="",  # Se actualizará después
        file_name=filename,
        file_type=file_type,
        image=image_data
    )
    db.session.add(new_image)
    db.session.flush()

    # Generar URL de descarga
    download_url = f"http://127.0.0.1:5001/api/recipe_images/download/{new_image.id}"
    new_image.download_url = download_url

    # Confirmar la transacción
    db.session.commit()

    return jsonify({
        "message": "Receta e imagen guardadas",
        "data": recipe_schema.dump(new_recipe)
    }), 201

@recipe_routes.route('/save', methods=['POST'])
def save_recipe():
    data = request.get_json()
    titulo = data.get('titulo')
    descripcion = data.get('descripcion')
    ingredientes = data.get('ingredientes')
    preparacion = data.get('preparacion')

    if not all([titulo]):
        return jsonify({"error": "Faltan datos requeridos: titulo"}), 400

    new_recipe = Recipe(
        titulo=titulo,
        descripcion=descripcion,
        ingredientes=ingredientes,
        preparacion=preparacion
    )
    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({"message": "Receta guardada", "data": recipe_schema.dump(new_recipe)}), 201

@recipe_routes.route('/update', methods=['PUT'])
def update_recipe():
    data = request.get_json()
    id = data.get('id')
    titulo = data.get('titulo')
    descripcion = data.get('descripcion')
    ingredientes = data.get('ingredientes')
    preparacion = data.get('preparacion')

    if not id:
        return jsonify({"error": "Falta el campo id"}), 400

    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    if titulo:
        recipe.titulo = titulo
    if descripcion is not None:
        recipe.descripcion = descripcion
    if ingredientes is not None:
        recipe.ingredientes = ingredientes
    if preparacion is not None:
        recipe.preparacion = preparacion

    db.session.commit()
    return jsonify({"message": "Receta actualizada", "data": recipe_schema.dump(recipe)}), 200

@recipe_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Receta eliminada"}), 200