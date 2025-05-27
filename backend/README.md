# Endpoints API rest

## AuthApi.py

- Crear un nuevo usuario.<br>
  [**POST** /api/auth/register](http://127.0.0.1:5001/api/auth/register)

  ```json
  {
    "nombre": "Juan Pérez",
    "email": "juan.perez@example.com",
    "contraseña": "password123"
  }
  ```

- Iniciar Sesión con email y contraseña.<br>
  [**POST** /api/auth/login](http://127.0.0.1:5001/api/auth/login)

  ```json
  {
    "email": "juan.perez@example.com",
    "contraseña": "password123"
  }
  ```

## RecipeApi.py

- Crear una nueva receta.<br>
  [POST /api/recipes/save](http://127.0.0.1:5001/api/recipes/save)

  ```json
  {
    "titulo": "Tarta de Manzana",
    "descripcion": "Deliciosa tarta de manzana casera.",
    "ingredientes": "Manzanas, harina, azúcar, mantequilla",
    "preparacion": "Mezclar ingredientes, hornear por 40 minutos."
  }
  ```

- Actualizar un receta.<br>
  [PUT /api/recipes/update](http://127.0.0.1:5001/api/recipes/update)

  ```json
  {
    "id": 1,
    "titulo": "Tarta de Manzana Mejorada",
    "descripcion": "Tarta de manzana con un toque de canela.",
    "ingredientes": "Manzanas, harina, azúcar, mantequilla, canela",
    "preparacion": "Mezclar ingredientes, hornear por 45 minutos."
  }
  ```

- Eliminar una receta.<br>
  [DELETE /api/recipes/delete/<id>](http://127.0.0.1:5001/api/recipes/delete/0)

## RatingApi.py

- Crear una calificación para una receta
  [POST /api/ratings/save](http://127.0.0.1:5001/api/ratings/save)

  ```json
  {
    "receta_id": 1,
    "calificacion": 4
  }
  ```

## CommentApi.py

- Crea un comentario para una receta.<br>
  [POST /api/comments/save](http://127.0.0.1:5001/api/comments/save)

  ```json
  {
    "receta_id": 1,
    "contenido": "¡Deliciosa receta, la probaré pronto!"
  }
  ```

- Actualizar un comentario.<br>
  [PUT /api/comments/update](http://127.0.0.1:5001/api/comments/update)

  ```json
  {
    "id": 1,
    "contenido": "Actualicé mi comentario: ¡fue increíble!"
  }
  ```

- Eliminar un comentario.<br>
  [DELETE /api/comments/delete/<id>](http://127.0.0.1:5001/api/comments/delete/0)
