from flask import Blueprint, request, jsonify
from config.db import db
from models.RecipeImageModel import RecipeImage, recipe_image_schema, recipe_images_schema
from models.RecipeModel import Recipe
import os
from werkzeug.utils import secure_filename

recipe_image_routes = Blueprint('recipe_image_routes', __name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads/recipe_images'  # Directory to store images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@recipe_image_routes.route('/', methods=['GET'])
def get_recipe_images():
    images = RecipeImage.query.all()
    return jsonify({"data": recipe_images_schema.dump(images)})

@recipe_image_routes.route('/save', methods=['POST'])
def save_recipe_image():
    # Check for required fields
    if 'receta_id' not in request.form or 'image' not in request.files:
        return jsonify({"error": "Faltan datos requeridos: receta_id o image"}), 400

    receta_id = request.form['receta_id']
    
    # Validate receta_id
    if not Recipe.query.get(receta_id):
        return jsonify({"error": "Receta no encontrada"}), 404

    # Handle file upload
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó ningún archivo"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Formato de archivo no permitido"}), 400

    # Secure filename and save file
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Generate download URL (assuming the server hosts the files)
    download_url = f"http://localhost:5001/{UPLOAD_FOLDER}/{filename}"
    file_type = file.mimetype

    # Save to database
    new_image = RecipeImage(
        receta_id=receta_id,
        downloadUrl=download_url,
        file_name=filename,
        file_type=file_type
    )
    db.session.add(new_image)
    db.session.commit()

    return jsonify({"message": "Imagen guardada", "data": recipe_image_schema.dump(new_image)}), 201

@recipe_image_routes.route('/delete/<id>', methods=['DELETE'])
def delete_recipe_image(id):
    image = RecipeImage.query.get(id)
    if not image:
        return jsonify({"error": "Imagen no encontrada"}), 404

    # Delete file from storage
    file_path = os.path.join(UPLOAD_FOLDER, image.file_name)
    if os.path.exists(file_path):
        os.remove(file_path)

    db.session.delete(image)
    db.session.commit()
    return jsonify({"message": "Imagen eliminada"})