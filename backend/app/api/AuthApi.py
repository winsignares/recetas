from flask import Blueprint, request, jsonify
from config.db import db
from models.UsersModel import User, user_schema
from datetime import datetime, timedelta
import jwt
import bcrypt
from config.db import app

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    nombre = request.json.get('nombre')
    email = request.json.get('email')
    contraseña = request.json.get('contraseña')

    if not all([nombre, email, contraseña]):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "El correo ya está registrado"}), 400

    hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_user = User(
        nombre=nombre,
        email=email,
        contraseña=hashed_password,
        fecha_registro=datetime.utcnow(),
    )
    db.session.add(new_user)
    db.session.commit()

    token = jwt.encode({
        'id': new_user.id,
        'email': new_user.email,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        "message": "Usuario registrado con éxito",
        "user": user_schema.dump(new_user),
        "token": token
    }), 201

@auth_routes.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    contraseña = request.json.get('contraseña')

    if not all([email, contraseña]):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.checkpw(contraseña.encode('utf-8'), user.contraseña.encode('utf-8')):
        return jsonify({"error": "Credenciales inválidas"}), 401

    token = jwt.encode({
        'id': user.id,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        "message": "Inicio de sesión exitoso",
        "user": user_schema.dump(user),
        "token": token
    })