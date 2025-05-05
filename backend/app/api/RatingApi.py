from flask import Blueprint, request, jsonify
from config.db import db
from models.RatingModel import Rating, rating_schema, ratings_schema
from models.RecipeModel import Recipe

rating_routes = Blueprint('rating_routes', __name__)

@rating_routes.route('/', methods=['GET'])
def get_ratings():
    ratings = Rating.query.all()
    return jsonify({"data": ratings_schema.dump(ratings)})

@rating_routes.route('/save', methods=['POST'])
def save_rating():
    data = request.json
    required_fields = ['usuario_id', 'receta_id', 'calificacion']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    if not (1 <= data['calificacion'] <= 5):
        return jsonify({"error": "Calificación debe estar entre 1 y 5"}), 400

    if Rating.query.filter_by(usuario_id=data['usuario_id'], receta_id=data['receta_id']).first():
        return jsonify({"error": "El usuario ya calificó esta receta"}), 400

    new_rating = Rating(
        usuario_id=data['usuario_id'],
        receta_id=data['receta_id'],
        calificacion=data['calificacion']
    )
    db.session.add(new_rating)

    # Update recipe's promedio_calificacion
    recipe = Recipe.query.get(data['receta_id'])
    ratings = Rating.query.filter_by(receta_id=data['receta_id']).all()
    recipe.promedio_calificacion = sum(r.calificacion for r in ratings) / len(ratings)
    db.session.commit()

    return jsonify({"message": "Calificación guardada", "data": rating_schema.dump(new_rating)}), 201

@rating_routes.route('/delete/<id>', methods=['DELETE'])
def delete_rating(id):
    rating = Rating.query.get(id)
    if not rating:
        return jsonify({"error": "Calificación no encontrada"}), 404

    recipe = Recipe.query.get(rating.receta_id)
    db.session.delete(rating)

    # Update recipe's promedio_calificacion
    ratings = Rating.query.filter_by(receta_id=recipe.id).all()
    recipe.promedio_calificacion = sum(r.calificacion for r in ratings) / len(ratings) if ratings else None
    db.session.commit()

    return jsonify({"message": "Calificación eliminada"})