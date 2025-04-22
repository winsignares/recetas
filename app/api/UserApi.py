from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import db, app, ma
from models.UsersModel import Users, UsersSchema

usuario_schema = UsersSchema()
usuarios_schema = UsersSchema(many=True)

ruta_user = Blueprint("ruta_user", __name__)

@ruta_user.route("/user", methods=['GET'])
def alluser():
    resultall = Users.query.all()
    resp = usuarios_schema.dump(resultall)  
    return jsonify(resp)

@ruta_user.route("/saveUser", methods=['POST'])
def saveuser():
    fullname = request.json.get('fullname')
    email = request.json.get('email')

    if not fullname or not email:
        return jsonify({"error": "Faltan datos"}), 400

    newuser = Users(fullname, email)
    db.session.add(newuser)
    db.session.commit()
    return jsonify({"message": "Usuario guardado con éxito"})

@ruta_user.route("/deleteUser", methods=['DELETE'])
def deleteuser():  
    id = request.json.get('id')
    user = Users.query.get(id)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado con éxito"})
