from flask import Flask, request, redirect, render_template
from flask_cors import CORS
from config.db import app, db

CORS(app, supports_credentials=True)

from api.UserApi import user_routes
from api.AuthApi import auth_routes
from api.RecipeApi import recipe_routes
from api.RecipeImageApi import recipe_image_routes
from api.CommentApi import comment_routes
from api.RatingApi import rating_routes

with app.app_context():
    db.create_all()

# Registramos las rutas con blueprint
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(user_routes, url_prefix='/api/user')
app.register_blueprint(recipe_routes, url_prefix='/api/recipes')
app.register_blueprint(recipe_image_routes, url_prefix='/api/recipe_images')
app.register_blueprint(comment_routes, url_prefix='/api/comments')
app.register_blueprint(rating_routes, url_prefix='/api/ratings')


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")