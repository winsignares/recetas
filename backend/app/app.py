from flask import Flask, request, redirect, render_template, send_from_directory
from config.db import app, db
import os

from api.UserApi import user_routes
from api.AuthApi import auth_routes
from api.CategoryApi import category_routes
from api.RecipeApi import recipe_routes
from api.RecipeImageApi import recipe_image_routes
from api.FavoriteApi import favorite_routes
from api.CommentApi import comment_routes
from api.RatingApi import rating_routes
from api.ProfilePictureApi import profile_picture_routes

with app.app_context():
    db.create_all()

# Registramos las rutas con blueprint
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(user_routes, url_prefix='/api/user') # localhost:5000/api/user
app.register_blueprint(category_routes, url_prefix='/api/categories')
app.register_blueprint(recipe_routes, url_prefix='/api/recipes')
app.register_blueprint(recipe_image_routes, url_prefix='/api/recipe_images')
app.register_blueprint(favorite_routes, url_prefix='/api/favorites')
app.register_blueprint(comment_routes, url_prefix='/api/comments')
app.register_blueprint(rating_routes, url_prefix='/api/ratings')
app.register_blueprint(profile_picture_routes, url_prefix='/api/profile_pictures')

@app.route('/uploads/<path:filename>')
def serve_uploaded_file(filename):
    uploads_dir = os.path.join(app.root_path, 'uploads')
    return send_from_directory(uploads_dir, filename)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")