from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import db, app, ma

from models.UsersModel import Users, UsersSchema

usuario_schema = UsersSchema()
usuarios_schema = UsersSchema(many=True)

ruta_user = Blueprint("ruta_user", __name__)

@ruta_user.route("/user", methods=['GET'])
def alluser():
    resultall = Users.query.all()
    resp = usuarios_schema(resultall)
    return jsonify(resp)


@ruta_user.route("/saveUser", methods=['POST'])
def saveuser():
    fullname = request.json['fullname']
    email = request.json['email']
    newuser = Users(fullname, email)
    db.session.add(newuser)
    db.session.commit()
    return "datos guardado con éxito"


@ruta_user.route("/deleteUser", methods=['DELETE'])
def alluser():
    id = request.json['id']
    user = Users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "dato eliminado con éxito"