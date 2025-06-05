from flask import Blueprint, request, jsonify
from config.db import db
from models.RatingModel import Rating, rating_schema, ratings_schema
from models.RecipeModel import Recipe
from models.UsersModel import User
from sqlalchemy.sql import func

rating_routes = Blueprint('rating_routes', __name__)

@rating_routes.route('/', methods=['GET'])
def get_ratings():
    ratings = Rating.query.all()
    return jsonify({"data": ratings_schema.dump(ratings)})

@rating_routes.route('/save', methods=['POST'])
def save_rating():
    data = request.get_json()
    receta_id = data.get('receta_id')
    calificacion = data.get('calificacion')

    # Valida los campos requeridos
    if not all([receta_id, calificacion]):
        return jsonify({"error": "Faltan datos requeridos: receta_id o calificacion"}), 400

    if not Recipe.query.get(receta_id):
        return jsonify({"error": "Receta no encontrada"}), 404

    # Validar calificación entre 1 y 5
    if not isinstance(calificacion, int) or calificacion < 1 or calificacion > 5:
        return jsonify({"error": "La calificación debe ser un entero entre 1 y 5"}), 400

    # Create new rating
    new_rating = Rating(
        receta_id=receta_id,
        calificacion=calificacion
    )
    db.session.add(new_rating)

    avg_rating = db.session.query(func.avg(Rating.calificacion)).filter(Rating.receta_id == receta_id).scalar()
    recipe = Recipe.query.get(receta_id)
    recipe.promedio_calificacion = avg_rating if avg_rating else None

    db.session.commit()

    return jsonify({"message": "Calificación guardada", "data": rating_schema.dump(new_rating)}), 201

@rating_routes.route('/delete/<id>', methods=['DELETE'])
def delete_rating(id):
    rating = Rating.query.get(id)
    if not rating:
        return jsonify({"error": "Calificación no encontrada"}), 404

    receta_id = rating.receta_id
    db.session.delete(rating)

   
    avg_rating = db.session.query(func.avg(Rating.calificacion)).filter(Rating.receta_id == receta_id).scalar()
    recipe = Recipe.query.get(receta_id)
    recipe.promedio_calificacion = avg_rating if avg_rating else None

    db.session.commit()
    return jsonify({"message": "Calificación eliminada"}), 200