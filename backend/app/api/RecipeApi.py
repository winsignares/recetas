from flask import Blueprint, request, jsonify
from config.db import db
from models.RecipeModel import Recipe, recipe_schema, recipes_schema
from models.UsersModel import User
from models.RecipeImageModel import RecipeImage
from werkzeug.utils import secure_filename
from .RecipeImageApi import allowed_file
import time

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

    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    ingredientes = request.form.get('ingredientes')
    preparacion = request.form.get('preparacion')

    if not titulo:
        return jsonify({"error": "Faltan datos requeridos: titulo"}), 400

    new_recipe = Recipe(
        titulo=titulo,
        descripcion=descripcion,
        ingredientes=ingredientes,
        preparacion=preparacion
    )
    db.session.add(new_recipe)
    db.session.flush() 

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
        download_url="", 
        file_name=filename,
        file_type=file_type,
        image=image_data
    )
    db.session.add(new_image)
    db.session.flush()

    download_url = f"http://127.0.0.1:5001/api/recipe_images/download/{new_image.id}?t={int(time.time())}"
    new_image.download_url = download_url

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


@recipe_routes.route('/update_with_image/<int:id>', methods=['PUT'])
def update_recipe_with_image(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    if 'titulo' not in request.form:
        return jsonify({"error": "Faltan datos requeridos: titulo"}), 400

    recipe.titulo = request.form.get('titulo')
    recipe.descripcion = request.form.get('descripcion')
    recipe.ingredientes = request.form.get('ingredientes')
    recipe.preparacion = request.form.get('preparacion')

    if 'image' in request.files and request.files['image'].filename != '':
        file = request.files['image']
        if not allowed_file(file.filename):
            return jsonify({"error": "Formato de archivo no permitido"}), 400

        filename = secure_filename(file.filename)
        file_type = file.mimetype
        image_data = file.read()

        existing_image = RecipeImage.query.filter_by(receta_id=recipe.id).first()
        if existing_image:
            existing_image.file_name = filename
            existing_image.file_type = file_type
            existing_image.image = image_data
            existing_image.download_url = f"http://127.0.0.1:5001/api/recipe_images/download/{existing_image.id}?t={int(time.time())}"
        else:
            new_image = RecipeImage(
                receta_id=recipe.id,
                download_url="",
                file_name=filename,
                file_type=file_type,
                image=image_data
            )
            db.session.add(new_image)
            db.session.flush()
            new_image.download_url = f"http://127.0.0.1:5001/api/recipe_images/download/{new_image.id}?t={int(time.time())}"

    try:
        db.session.commit()
        return jsonify({
            "message": "Receta e imagen actualizadas",
            "data": recipe_schema.dump(recipe)
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error al actualizar: {str(e)}"}), 500


@recipe_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    if not recipe:
        return jsonify({"error": "Receta no encontrada"}), 404

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Receta eliminada"}), 200