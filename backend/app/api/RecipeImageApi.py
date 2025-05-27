from flask import Blueprint, request, jsonify, send_file
from config.db import db
from models.RecipeImageModel import RecipeImage, recipe_image_schema, recipe_images_schema
from models.RecipeModel import Recipe
from werkzeug.utils import secure_filename
import io

recipe_image_routes = Blueprint('recipe_image_routes', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@recipe_image_routes.route('/', methods=['GET'])
def get_recipe_images():
    images = RecipeImage.query.all()
    return jsonify({"data": recipe_images_schema.dump(images)}), 200

@recipe_image_routes.route('/<id>', methods=['GET'])
def get_recipe_image(id):
    try:
        image_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    image = RecipeImage.query.get(image_id)
    if not image:
        return jsonify({"error": "Imagen no encontrada"}), 404

    return jsonify({"data": recipe_image_schema.dump(image)}), 200

@recipe_image_routes.route('/save', methods=['POST'])
def save_recipe_image():
    if 'receta_id' not in request.form or 'image' not in request.files:
        return jsonify({"error": "Faltan datos requeridos: receta_id o image"}), 400

    receta_id = request.form['receta_id']
    
    if not Recipe.query.get(receta_id):
        return jsonify({"error": "Receta no encontrada"}), 404

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó ningún archivo"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Formato de archivo no permitido"}), 400

    filename = secure_filename(file.filename)
    file_type = file.mimetype
    image_data = file.read() 

    
    new_image = RecipeImage(
        receta_id=receta_id,
        download_url="", 
        file_name=filename,
        file_type=file_type,
        image=image_data
    )
    db.session.add(new_image)
    db.session.flush() 

    # Generate download URL
    download_url = f"http://127.0.0.1:5001/api/recipe_images/download/{new_image.id}"
    new_image.download_url = download_url

    db.session.commit()

    return jsonify({"message": "Imagen guardada", "data": recipe_image_schema.dump(new_image)}), 201

@recipe_image_routes.route('/download/<id>', methods=['GET'])
def download_recipe_image(id):
    try:
        image_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    image = RecipeImage.query.get(image_id)
    if not image:
        return jsonify({"error": "Imagen no encontrada"}), 404

    # Return the binary image data
    return send_file(
        io.BytesIO(image.image),
        mimetype=image.file_type,
        as_attachment=False,
        download_name=image.file_name
    )

@recipe_image_routes.route('/update/<id>', methods=['PUT'])
def update_recipe_image(id):
    try:
        image_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    image = RecipeImage.query.get(image_id)
    if not image:
        return jsonify({"error": "Imagen no encontrada"}), 404

    if 'image' not in request.files:
        return jsonify({"error": "Falta el archivo de imagen"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó ningún archivo"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Formato de archivo no permitido"}), 400

    filename = secure_filename(file.filename)
    file_type = file.mimetype
    image_data = file.read()

    image.file_name = filename
    image.file_type = file_type
    image.image = image_data
    image.download_url = f"/api/recipe_images/download/{image.id}"

    db.session.commit()
    return jsonify({"message": "Imagen actualizada", "data": recipe_image_schema.dump(image)}), 200

@recipe_image_routes.route('/delete/<id>', methods=['DELETE'])
def delete_recipe_image(id):
    try:
        image_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    image = RecipeImage.query.get(image_id)
    if not image:
        return jsonify({"error": "Imagen no encontrada"}), 404

    db.session.delete(image)
    db.session.commit()
    return jsonify({"message": "Imagen eliminada"}), 200