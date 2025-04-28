from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import db, app, ma
from models.TaskModel import Task, TaskSchema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

ruta_task = Blueprint("ruta_task", __name__)

@ruta_task.route("/task", methods=['GET'])
def alltask():
    resultall = Task.query.all()
    resp = tasks_schema.dump(resultall) 
    return jsonify(resp)

@ruta_task.route("/saveTask", methods=['POST'])
def savetask():
    name_task = request.json.get('nametask')
    id_user_fk = request.json.get('id_user_fk')
    id_category_fk = request.json.get('id_category_fk')

    if not all([name_task, id_user_fk, id_category_fk]):
        return jsonify({"error": "Faltan datos"}), 400

    newTask = Task(name_task, id_user_fk, id_category_fk)
    db.session.add(newTask)
    db.session.commit()
    return jsonify({"message": "Tarea guardada con éxito"})

@ruta_task.route("/deleteTask/<id>", methods=['DELETE'])
def deletetask(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Tarea eliminada con éxito"})
