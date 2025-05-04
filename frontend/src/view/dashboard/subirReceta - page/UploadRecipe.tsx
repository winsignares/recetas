import { useState } from "react";

export default function UploadRecipe() {
  const [fileName, setFileName] = useState("Ningún archivo elegido");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFileName(e.target.files[0].name);
    } else {
      setFileName("Ningún archivo elegido");
    }
  };

  return (
    <div className="min-h-screen w-full p-4 md:p-8">

      <form className="grid grid-cols-1 md:grid-cols-2 gap-6 bg-blue-100 rounded-xl p-6 shadow-md">
        <div className="flex flex-col gap-2">
          <label htmlFor="titulo" className="font-medium text-blue-900">Título de la receta</label>
          <input
            type="text"
            id="titulo"
            className="rounded-xl border border-blue-200 bg-white px-4 py-2 shadow-sm"
          />
        </div>

        <div className="flex flex-col gap-2">
          <label htmlFor="autor" className="font-medium text-blue-900">Autor</label>
          <input
            type="text"
            id="autor"
            className="rounded-xl border border-blue-200 bg-white px-4 py-2 shadow-sm"
          />
        </div>

        <div className="md:col-span-2 flex flex-col gap-2">
          <label htmlFor="contenido" className="font-medium text-blue-900">Contenido</label>
          <textarea
            id="contenido"
            rows={6}
            className="rounded-xl border bg-white border-blue-200 px-4 py-2 shadow-sm resize-y"
          ></textarea>
        </div>

        <div className="flex flex-col gap-2">
          <label htmlFor="categoria" className="font-medium text-blue-900">Categoría</label>
          <input
            type="text"
            id="categoria"
            className="rounded-xl border border-blue-200 bg-white px-4 py-2 shadow-sm"
          />
        </div>

        <div className="flex flex-col gap-2">
          <label className="font-medium text-blue-900">Imagen de portada</label>
          <div className="flex items-center gap-4">
            <div className="w-16 h-16 bg-gray-200 rounded-xl flex items-center justify-center">
              📷
            </div>
            <div className="flex-1">
              <input
                type="file"
                accept="image/*"
                onChange={handleFileChange}
                className="hidden"
                id="fileInput"
              />
              <label
                htmlFor="fileInput"
                className="cursor-pointer rounded-md border border-green-500 px-4 py-2 text-green-600 hover:bg-green-100"
              >
                Elija archivo
              </label>
              <p className="text-sm mt-1 text-gray-600">{fileName}</p>
              <p className="text-xs text-gray-400 italic mt-1">
                Cargue una imagen de tamaño inferior a 100 KB
              </p>
            </div>
          </div>
        </div>

        <div className="md:col-span-2">
          <button
            type="submit"
            className="bg-[#0A4486] text-white px-6 py-2 rounded-md hover:bg-[#1559A5] 
              cursor-pointer transition-colors duration-200"
          >
            + Subir nueva receta
          </button>
        </div>
      </form>
    </div>
  );
}
