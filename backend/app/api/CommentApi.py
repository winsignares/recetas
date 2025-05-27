from flask import Blueprint, request, jsonify
from config.db import db
from models.CommentModel import Comment, comment_schema, comments_schema
from datetime import datetime

comment_routes = Blueprint('comment_routes', __name__)

@comment_routes.route('/', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify({"data": comments_schema.dump(comments)})

@comment_routes.route('/save/<int:receta_id>', methods=['POST'])
def save_comment(receta_id):
    data = request.json
    if 'contenido' not in data:
        return jsonify({"error": "Falta el contenido del comentario"}), 400

    new_comment = Comment(
        receta_id=receta_id,
        contenido=data['contenido']
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comentario guardado", "data": comment_schema.dump(new_comment)}), 201

@comment_routes.route('/update/<int:id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "Comentario no encontrado"}), 404

    data = request.json
    if 'contenido' in data:
        comment.contenido = data['contenido']

    db.session.commit()
    return jsonify({"message": "Comentario actualizado", "data": comment_schema.dump(comment)})


@comment_routes.route('/delete/<id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "Comentario no encontrado"}), 404
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comentario eliminado"})