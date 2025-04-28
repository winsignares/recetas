from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import db, app, ma

from models.CategoryModel import Category, CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

ruta_category = Blueprint("ruta_category", __name__)

@ruta_category.route("/category", methods=['GET'])
def allcategories():
    resultall = Category.query.all()
    resp = categories_schema.dump(resultall)  
    return jsonify(resp)

@ruta_category.route("/createCategory", methods=['POST'])  
def categorysave():
    name = request.json.get('namecategory')
    if not name:
        return jsonify({"error": "namecategory es requerido"}), 400
    newcategory = Category(name)
    db.session.add(newcategory)
    db.session.commit()
    return jsonify({"message": "Categoría guardada con éxito"})

@ruta_category.route("/deleteCategory/<id>", methods=['DELETE'])
def deletecategory(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"error": "Categoría no encontrada"}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Categoría eliminada con éxito"})

@ruta_category.route("/updateCategory", methods=['PUT']) 
def categoryupdate():
    id = request.json.get('id')
    name = request.json.get('namecategory')
    category = Category.query.get(id)
    if not category:
        return jsonify({"error": "Categoría no encontrada"}), 404
    category.namecategory = name
    db.session.commit()
    return jsonify({"message": "Categoría actualizada con éxito"})
