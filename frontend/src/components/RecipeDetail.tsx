import { Link, useNavigate } from 'react-router-dom';
import { Receta } from '../types/index';
import { useMutation } from '@tanstack/react-query';
import { deleteRecipe } from '@/api/recipeApi';


type RecipeDetailProps = {
  data: Receta
}

export default function RecipeDetail({ data }: RecipeDetailProps) {
  const navigate = useNavigate()
  
  const ingredientesArray: string[] = data.ingredientes.split(",").map((ing) => ing.trim()).filter((ing) => ing.length > 0)

  const { mutate } = useMutation({
    mutationFn: deleteRecipe
  })
  
  const handleDelete = (recetaId: Receta['id']) => {
    mutate(recetaId)
    navigate('/recetas')
  }

  return (
    <section>
      <div className='relative flex gap-4 justify-end mb-6'>
        <Link
          to='/'
          className='bg-[#0A4486] p-2 hover:bg-[#1559A5] text-white font-bold transition-colors 
          rounded cursor-pointer'
        >Actualizar</Link>
        <button
          className='bg-red-500 p-2 hover:bg-red-400 text-white font-bold transition-colors 
          rounded cursor-pointer'
          onClick={() => handleDelete(data.id)}
        >Eliminar</button>
      </div>
      <h1 className="text-3xl md:text-4xl font-semibold mb-4">
        {data.titulo}
      </h1>
      
      <img
        src={data.imagenes[0]?.download_url}
        alt={data.imagenes[0]?.file_name}
        className="rounded-xl w-full object-cover mb-6"
      />
      <p className="text-2xl font-bold text-gray-700 mb-4">
        {data.descripcion}
      </p>
      <p className='text-2xl font-bold text-gray-700 mb-2'>
        Ingredientes
      </p>
      
      <ul className='list-disc ml-1 pl-3 mb-4'>
        {ingredientesArray.map((ingrediente, index) => (
          <li key={index}>{ ingrediente }</li>
        ))}
      </ul>
      
      <p className='text-2xl font-bold text-gray-700 mb-2'>
        Preparación
      </p>
      <p className="text-gray-700 mb-4">
        {data.preparacion}
      </p>
    </section>
  );
}
