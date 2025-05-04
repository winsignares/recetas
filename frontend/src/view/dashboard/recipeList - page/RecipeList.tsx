// src/pages/dashboard/recetas.tsx
import { Pencil, Trash2 } from "lucide-react";

export default function RecipeList() {
  return (
    <div className="flex flex-col gap-4 p-4 md:p-8 w-full">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center">
        <h2 className="text-3xl font-semibold text-slate-800">Recetas subidas</h2>
        
      </div>

      <div className="bg-blue-50 rounded-xl p-4 shadow w-full overflow-x-auto mt-6">
        <table className="w-full min-w-[600px] text-left border border-slate-200">
          <thead>
            <tr className="bg-white border-b text-slate-700">
              <th className="py-2 px-4 font-medium">Título</th>
              <th className="py-2 px-4 font-medium">Autor</th>
              <th className="py-2 px-4 font-medium">Categoría</th>
              <th className="py-2 px-4 font-medium">Fecha</th>
              <th className="py-2 px-4 font-medium">Acción</th>
            </tr>
          </thead>
          <tbody>
            {[
              { titulo: "Paella", autor: "Carlos", categoria: "Comida", fecha: "2025-05-01" },
              { titulo: "Tacos", autor: "Luis", categoria: "Mexicana", fecha: "2025-05-02" },
              { titulo: "Sushi", autor: "Ana", categoria: "Japonesa", fecha: "2025-05-03" },
            ].map((receta, i) => (
              <tr key={i} className="border-t hover:bg-slate-100">
                <td className="py-2 px-4">{receta.titulo}</td>
                <td className="py-2 px-4">{receta.autor}</td>
                <td className="py-2 px-4">{receta.categoria}</td>
                <td className="py-2 px-4">{receta.fecha}</td>
                <td className="py-2 px-4 flex gap-2">
                  <Pencil className="w-5 h-5 text-blue-600 cursor-pointer" />
                  <Trash2 className="w-5 h-5 text-red-500 cursor-pointer" />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
