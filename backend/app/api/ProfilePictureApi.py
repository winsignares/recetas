from flask import Blueprint, request, jsonify, send_file
from config.db import db
from models.ProfilePictureModel import ProfilePicture, profile_picture_schema, profile_pictures_schema
from models.UsersModel import User
from werkzeug.utils import secure_filename
import io

profile_picture_routes = Blueprint('profile_picture_routes', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@profile_picture_routes.route('/', methods=['GET'])
def get_profile_pictures():
    pictures = ProfilePicture.query.all()
    return jsonify({"data": profile_pictures_schema.dump(pictures)}), 200

@profile_picture_routes.route('/<id>', methods=['GET'])
def get_profile_picture(id):
    try:
        picture_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    picture = ProfilePicture.query.get(picture_id)
    if not picture:
        return jsonify({"error": "Foto de perfil no encontrada"}), 404

    return jsonify({"data": profile_picture_schema.dump(picture)}), 200

@profile_picture_routes.route('/save', methods=['POST'])
def save_profile_picture():
    if 'usuario_id' not in request.form or 'image' not in request.files:
        return jsonify({"error": "Faltan datos requeridos: usuario_id o image"}), 400

    usuario_id = request.form['usuario_id']
    
    if not User.query.get(usuario_id):
        return jsonify({"error": "Usuario no encontrado"}), 404
    if ProfilePicture.query.filter_by(usuario_id=usuario_id).first():
        return jsonify({"error": "El usuario ya tiene una foto de perfil"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó ningún archivo"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Formato de archivo no permitido"}), 400

    filename = secure_filename(file.filename)
    file_type = file.mimetype
    image_data = file.read()

    new_picture = ProfilePicture(
        usuario_id=usuario_id,
        download_url="",  
        file_name=filename,
        file_type=file_type,
        image=image_data
    )
    db.session.add(new_picture)
    db.session.flush() 

    download_url = f"/api/profile_pictures/download/{new_picture.id}"
    new_picture.download_url = download_url

    db.session.commit()

    return jsonify({"message": "Foto de perfil guardada", "data": profile_picture_schema.dump(new_picture)}), 201

@profile_picture_routes.route('/download/<id>', methods=['GET'])
def download_profile_picture(id):
    try:
        picture_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    picture = ProfilePicture.query.get(picture_id)
    if not picture:
        return jsonify({"error": "Foto de perfil no encontrada"}), 404

    return send_file(
        io.BytesIO(picture.image),
        mimetype=picture.file_type,
        as_attachment=False,
        download_name=picture.file_name
    )

@profile_picture_routes.route('/update/<id>', methods=['PUT'])
def update_profile_picture(id):
    try:
        picture_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    picture = ProfilePicture.query.get(picture_id)
    if not picture:
        return jsonify({"error": "Foto de perfil no encontrada"}), 404

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

    picture.file_name = filename
    picture.file_type = file_type
    picture.image = image_data
    picture.download_url = f"/api/profile_pictures/download/{picture.id}"

    db.session.commit()
    return jsonify({"message": "Foto de perfil actualizada", "data": profile_picture_schema.dump(picture)}), 200

@profile_picture_routes.route('/delete/<id>', methods=['DELETE'])
def delete_profile_picture(id):
    try:
        picture_id = int(id)
    except ValueError:
        return jsonify({"error": "El id debe ser un número entero"}), 400

    picture = ProfilePicture.query.get(picture_id)
    if not picture:
        return jsonify({"error": "Foto de perfil no encontrada"}), 404

    db.session.delete(picture)
    db.session.commit()
    return jsonify({"message": "Foto de perfil eliminada"}), 200