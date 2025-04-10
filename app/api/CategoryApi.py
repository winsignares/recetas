from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import db, app, ma

from models.CategoryModel import Category, CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

ruta_category = Blueprint("ruta_category", __name__)

@ruta_category.route("/category", methods=['GET'])
def allcategories():
    resultall = Category.query.all()
    resp = categories_schema(resultall)
    return jsonify(resp)


@ruta_category.route("/saveCategory", methods=['POST'])
def categorysave():
    name = request.json['namecategory']
    newcategory = Category(name)
    db.session.add(newcategory)
    db.session.commit()
    return "datos guardado con éxito"


@ruta_category.route("/deleteCategory/<id>", methods=['DELETE'])
def deletecategory(id):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()
    return "dato eliminado con éxito"


@ruta_category.route("/saveCategory", methods=['POST'])
def categoryupdate():
    id = request.json['id']
    category = Category.query.get(id)
    category.namecategory = request.json['namecategory']
    db.session.add(category)
    db.session.commit()
    return "datos actualizados con éxito"