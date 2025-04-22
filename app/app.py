from flask import Flask, request, redirect, render_template
from config.db import app, db

from api.UserApi import ruta_user
from api.CategoryApi import ruta_category
from api.TaskApi import ruta_task

with app.app_context():
    db.create_all()

# Registramos las rutas con blueprint
app.register_blueprint(ruta_user, url_prefix='/api') # localhost:5000/api/user
app.register_blueprint(ruta_category, url_prefix='/api')
app.register_blueprint(ruta_task, url_prefix='/api')

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")