from flask import Blueprint, request, jsonify
from config.db import db
from models.UsersModel import User, user_schema, users_schema

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({"data": users_schema.dump(users)})

@user_routes.route('/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user_schema.dump(user))

@user_routes.route('/update', methods=['PUT'])
def update_user():
    id = request.json.get('id')
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    user.nombre = request.json.get('nombre', user.nombre)
    user.email = request.json.get('email', user.email)
    db.session.commit()
    return jsonify({"message": "Usuario actualizado", "data": user_schema.dump(user)})

@user_routes.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado"})