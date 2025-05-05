from flask import Blueprint, request, jsonify
from config.db import db
from models.CategoryModel import Category, category_schema, categories_schema

category_routes = Blueprint('category_routes', __name__)

@category_routes.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify({"data": categories_schema.dump(categories)})

@category_routes.route('/save', methods=['POST'])
def save_category():
    nombre = request.json.get('nombre')
    if not nombre:
        return jsonify({"error": "Nombre es requerido"}), 400
    new_category = Category(nombre)
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Categoría guardada", "data": category_schema.dump(new_category)}), 201

@category_routes.route('/update', methods=['PUT'])
def update_category():
    id = request.json.get('id')
    category = Category.query.get(id)
    if not category:
        return jsonify({"error": "Categoría no encontrada"}), 404
    category.nombre = request.json.get('nombre', category.nombre)
    db.session.commit()
    return jsonify({"message": "Categoría actualizada", "data": category_schema.dump(category)})

@category_routes.route('/delete/<id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"error": "Categoría no encontrada"}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Categoría eliminada"})