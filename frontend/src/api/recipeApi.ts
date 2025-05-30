import { Comment, FormReceta, Receta, RecetaResponseSchema, RecetasResponseSchema } from '@/types'
import axios from 'axios'

export const url = 'http://127.0.0.1:5001'

export async function getRecipes() {
  try {
    const { data } = await axios.get(`${url}/api/recipes`)
    const response = RecetasResponseSchema.safeParse(data)
    console.log(response);
    if (response.success) {
      return response.data
    }
  } catch (error) {
    console.log(error);
  }
}

export async function getRecipeById(id: Receta['id']) {
  try {
    const { data } = await axios.get(`${url}/api/recipes/${id}`)
    const response = RecetaResponseSchema.safeParse(data)
    if (response.success) {
      return response.data.data
    }
  } catch (error) {
    console.log(error);
  }
}

export async function createRecipe(formData: FormReceta) {
  try {
    const { data } = await axios.post(`${url}/api/recipes/save`, formData)
    return data.data
  } catch (error) {
    console.log(error);
  }
}

export async function createRecipeWithImage(formData: FormReceta, image: File) {
  const form = new FormData();
  form.append("titulo", formData.titulo);
  form.append("descripcion", formData.descripcion);
  form.append("ingredientes", formData.ingredientes);
  form.append("preparacion", formData.preparacion);
  form.append("image", image);

  try {
    const { data } = await axios.post(`${url}/api/recipes/save_with_image`, form, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return data.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function updateRecipeWithImage(id: Receta['id'], formData: FormReceta, image?: File) {
  const form = new FormData();
  form.append("titulo", formData.titulo);
  form.append("descripcion", formData.descripcion);
  form.append("ingredientes", formData.ingredientes);
  form.append("preparacion", formData.preparacion);
  if (image) {
    form.append("image", image);
  }

  try {
    const { data } = await axios.put(`${url}/api/recipes/update_with_image/${id}`, form, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return data.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function deleteRecipe(id: Receta['id']) {
  try {
    const { data } = await axios.delete(`${url}/api/recipes/delete/${id}`)
    console.log(data);
    return data.data
  } catch (error) {
    console.log(error);
  }
}

// images
export async function createImage(image: File, receta_id: number) {
  const formData = new FormData()
  formData.append("receta_id", receta_id.toString())
  formData.append("image", image)

  const response = await axios.post(`${url}/api/recipe_images/save`, formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    },
  });

  return response
}

// Comentarios
type CommentApiType = {
  commentFormData: Comment,
  receta_id: Receta['id']
}

export async function createComment({commentFormData, receta_id}: CommentApiType) {
  try {
    const { data } = await axios.post(`${url}/api/comments/save/${receta_id}`, commentFormData)
    const response = RecetaResponseSchema.safeParse(data)
    if (response.success) {
      return response.data.data
    }
  } catch (error) {
    console.log(error);
  }
}

export async function deleteComment(receta_id: Receta['id']) {
  try {
    const { data } = await axios.delete(`${url}/api/comments/delete/${receta_id}`)
    const response = RecetaResponseSchema.safeParse(data)
    if (response.success) {
      return response.data.data
    }
  } catch (error) {
    console.log(error);
  }
}