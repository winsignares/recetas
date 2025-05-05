from flask import Blueprint, request, jsonify
from config.db import db
from models.CommentModel import Comment, comment_schema, comments_schema
from datetime import datetime

comment_routes = Blueprint('comment_routes', __name__)

@comment_routes.route('/', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify({"data": comments_schema.dump(comments)})

@comment_routes.route('/save', methods=['POST'])
def save_comment():
    data = request.json
    required_fields = ['usuario_id', 'receta_id', 'contenido']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    new_comment = Comment(
        usuario_id=data['usuario_id'],
        receta_id=data['receta_id'],
        contenido=data['contenido'],
        fecha_comentario=datetime.utcnow()
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comentario guardado", "data": comment_schema.dump(new_comment)}), 201

@comment_routes.route('/update', methods=['PUT'])
def update_comment():
    id = request.json.get('id')
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "Comentario no encontrado"}), 404
    comment.contenido = request.json.get('contenido', comment.contenido)
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