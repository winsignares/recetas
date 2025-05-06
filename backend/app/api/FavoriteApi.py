from flask import Blueprint, request, jsonify
from config.db import db
from models.FavoriteModel import Favorite, favorite_schema, favorites_schema

favorite_routes = Blueprint('favorite_routes', __name__)

@favorite_routes.route('/', methods=['GET'])
def get_favorites():
    favorites = Favorite.query.all()
    return jsonify({"data": favorites_schema.dump(favorites)})

@favorite_routes.route('/save', methods=['POST'])
def save_favorite():
    usuario_id = request.json.get('usuario_id')
    receta_id = request.json.get('receta_id')
    if not all([usuario_id, receta_id]):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    if Favorite.query.filter_by(usuario_id=usuario_id, receta_id=receta_id).first():
        return jsonify({"error": "Favorito ya existe"}), 400

    new_favorite = Favorite(usuario_id, receta_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({"message": "Favorito guardado", "data": favorite_schema.dump(new_favorite)}), 201

@favorite_routes.route('/delete/<id>', methods=['DELETE'])
def delete_favorite(id):
    favorite = Favorite.query.get(id)
    if not favorite:
        return jsonify({"error": "Favorito no encontrado"}), 404
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Favorito eliminado"})