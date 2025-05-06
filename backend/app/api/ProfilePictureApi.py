from flask import Blueprint, request, jsonify
from config.db import db
from models.ProfilePictureModel import ProfilePicture, profile_picture_schema, profile_pictures_schema
from models.UsersModel import User
import os
from werkzeug.utils import secure_filename

profile_picture_routes = Blueprint('profile_picture_routes', __name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads/profile_pictures'  # Directory to store profile pictures
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@profile_picture_routes.route('/', methods=['GET'])
def get_profile_pictures():
    pictures = ProfilePicture.query.all()
    return jsonify({"data": profile_pictures_schema.dump(pictures)})

@profile_picture_routes.route('/save', methods=['POST'])
def save_profile_picture():
    # Check for required fields
    if 'usuario_id' not in request.form or 'image' not in request.files:
        return jsonify({"error": "Faltan datos requeridos: usuario_id o image"}), 400

    usuario_id = request.form['usuario_id']
    
    # Validate usuario_id
    if not User.query.get(usuario_id):
        return jsonify({"error": "Usuario no encontrado"}), 404
    if ProfilePicture.query.filter_by(usuario_id=usuario_id).first():
        return jsonify({"error": "El usuario ya tiene una foto de perfil"}), 400

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

    # Generate download URL
    download_url = f"http://localhost:5001/{UPLOAD_FOLDER}/{filename}"
    file_type = file.mimetype

    # Save to database
    new_picture = ProfilePicture(
        usuario_id=usuario_id,
        downloadUrl=download_url,
        file_name=filename,
        file_type=file_type
    )
    db.session.add(new_picture)
    db.session.commit()

    return jsonify({"message": "Foto de perfil guardada", "data": profile_picture_schema.dump(new_picture)}), 201

@profile_picture_routes.route('/update', methods=['PUT'])
def update_profile_picture():
    # Check for required fields
    if 'id' not in request.form:
        return jsonify({"error": "Faltan datos requeridos: id"}), 400

    picture = ProfilePicture.query.get(request.form['id'])
    if not picture:
        return jsonify({"error": "Foto de perfil no encontrada"}), 404

    # Handle file upload if provided
    if 'image' in request.files:
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No se seleccionó ningún archivo"}), 400
        if not allowed_file(file.filename):
            return jsonify({"error": "Formato de archivo no permitido"}), 400

        # Delete old file
        old_file_path = os.path.join(UPLOAD_FOLDER, picture.file_name)
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

        # Save new file
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Update metadata
        picture.downloadUrl = f"http://localhost:5001/{UPLOAD_FOLDER}/{filename}"
        picture.file_name = filename
        picture.file_type = file.mimetype

    db.session.commit()
    return jsonify({"message": "Foto de perfil actualizada", "data": profile_picture_schema.dump(picture)})

@profile_picture_routes.route('/delete/<id>', methods=['DELETE'])
def delete_profile_picture(id):
    picture = ProfilePicture.query.get(id)
    if not picture:
        return jsonify({"error": "Foto de perfil no encontrada"}), 404

    # Delete file from storage
    file_path = os.path.join(UPLOAD_FOLDER, picture.file_name)
    if os.path.exists(file_path):
        os.remove(file_path)

    db.session.delete(picture)
    db.session.commit()
    return jsonify({"message": "Foto de perfil eliminada"})