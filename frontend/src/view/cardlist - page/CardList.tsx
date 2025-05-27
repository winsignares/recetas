import { Link } from "react-router-dom";
import { useQuery } from '@tanstack/react-query'
import { getRecipes } from "@/api/recipeApi";

export default function CardList() {

  const { data } = useQuery({
    queryKey: ['recipes'],
    queryFn: getRecipes,
    refetchInterval: 10000
  })

  return (
    <div className="bg-white py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-2">Recetas</h2>
        <p className="text-center text-gray-500 max-w-2xl mx-auto mb-10">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim
        </p>
        <div className="mb-6 gap-6">
          <Link
            to='/dashboard/subir-receta'
            className="bg-[#0A4486] p-2 hover:bg-[#1559A5] text-white font-bold transition-colors rounded"
          >Subir receta</Link>
        </div>

        {!data?.data ? (
          <p className="text-center mx-auto mt-60 text-3xl font-bold">No hay recetas aún.</p>
        ) : (
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {data.data.map((recipe) => (
            <div
              key={recipe.id}
              className="bg-blue-50 rounded-2xl overflow-hidden shadow hover:shadow-lg transition-shadow duration-300"
            >
              <img
                src={recipe.imagenes[0]?.download_url}
                alt={recipe.titulo}
                className="w-full h-48 object-cover"
              />
              <div className="p-4">
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {recipe.titulo}
                </h3>
                <div className="flex justify-between items-center">
                  <Link to={`/${recipe.id}/receta-detalle`} className="text-blue-600 hover:underline">
                    Ver más
                  </Link>
                  <div className="flex mt-2 space-x-1">
                    <p>Comentarios</p>
                    <p className="ml-2 my-auto">({ Math.round(recipe.comentarios.length) })</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        )}
      </div>
    </div>
  );
}
