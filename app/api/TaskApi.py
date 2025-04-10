from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import db, app, ma

from models.TaskModel import Task, TaskSchema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

ruta_task = Blueprint("ruta_task", __name__)

@ruta_task.route("/task", methods=['GET'])
def alltask():
    resultall = Task.query.all()
    resp = TaskSchema(resultall)
    return jsonify(resp)


@ruta_task.route("/saveTask", methods=['POST'])
def savetask():
    name_task = request.json['nametask']
    id_user_fk = request.json['id_user_fk']
    id_category_fk = request.json['id_category_fk']
    newTask = Task(name_task, id_user_fk, id_category_fk)
    db.session.add(newTask)
    db.session.commit()
    return "datos guardado con éxito"


@ruta_task.route("/deleteTask/<id>", methods=['DELETE'])
def deletetask(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return "dato eliminado con éxito"