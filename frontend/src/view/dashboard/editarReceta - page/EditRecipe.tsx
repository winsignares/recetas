import ErrorMessage from "@/components/ErrorMessage";
import { FormReceta, formRecetaSchema } from "@/types";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useState, useEffect } from "react";
import { getRecipeById, updateRecipeWithImage } from "@/api/recipeApi";
import { useParams, useNavigate } from "react-router-dom";

export default function EditRecipe() {
  const queryClient = useQueryClient();

  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [file, setFile] = useState<File | null>(null);
  const [fileName, setFileName] = useState("Ningún archivo elegido");

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
    setValue
  } = useForm<FormReceta>({
    resolver: zodResolver(formRecetaSchema),
    defaultValues: {
      titulo: "",
      descripcion: "",
      ingredientes: "",
      preparacion: "",
    },
  });

  const { data: recipe, isLoading, error } = useQuery({
    queryKey: ['recipe', id],
    queryFn: () => getRecipeById(Number(id)),
    enabled: !!id,
  });

  useEffect(() => {
    if (recipe) {
      setValue("titulo", recipe.titulo);
      setValue("descripcion", recipe.descripcion);
      setValue("ingredientes", recipe.ingredientes);
      setValue("preparacion", recipe.preparacion);
      if (recipe.imagenes[0]?.file_name) {
        setFileName(recipe.imagenes[0].file_name);
      }
    }
  }, [recipe, setValue]);

  const updateRecipeWithImageMutation = useMutation({
    mutationFn: ({ id, formData, image }: { id: number; formData: FormReceta; image?: File }) =>
      updateRecipeWithImage(id, formData, image),
  });

  const onSubmit = async (formValues: FormReceta) => {
    if (!id) {
      alert("ID de receta no encontrado ❗");
      return;
    }

    try {
      await updateRecipeWithImageMutation.mutateAsync({
        id: Number(id),
        formData: formValues,
        image: file || undefined,
      });

      queryClient.invalidateQueries({queryKey: ['recipeDetail']})

      alert("Receta actualizada exitosamente ✅");
      reset();
      setFile(null);
      setFileName("Ningún archivo elegido");
      navigate(`/recetas`);
    } catch (error) {
      alert(error);
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setFileName(e.target.files[0].name);
    } else {
      setFile(null);
      setFileName("Ningún archivo elegido");
    }
  };

  if (isLoading) return <div>Cargando...</div>;
  if (error) return <div>Error al cargar la receta: {error.message}</div>;
  if (!recipe) return <div>Receta no encontrada</div>;

  return (
    <div className="min-h-screen w-full p-4 md:p-8 shadow-md">
      <h2 className="text-3xl font-bold text-[#0A4486]">Actualizar Receta</h2>

      <form
        className="grid grid-cols-1 md:grid-cols-2 gap-6 rounded-xl p-6 my-6 shadow-md"
        onSubmit={handleSubmit(onSubmit)}
        noValidate
      >
        <div className="flex flex-col gap-2">
          <label htmlFor="titulo" className="font-medium text-blue-900">
            Título de la receta
          </label>
          <input
            type="text"
            id="titulo"
            className="rounded-xl border border-blue-200 bg-white px-4 py-2 shadow-sm"
            placeholder="Ej. Tarta de Manzana"
            {...register("titulo")}
          />
          {errors.titulo && <ErrorMessage>{errors.titulo.message}</ErrorMessage>}
        </div>

        <div className="flex flex-col gap-2">
          <label htmlFor="descripcion" className="font-medium text-blue-900">
            Descripción
          </label>
          <input
            type="text"
            id="descripcion"
            className="rounded-xl border border-blue-200 bg-white px-4 py-2 shadow-sm"
            placeholder="Deliciosa tarta de manzana casera."
            {...register("descripcion")}
          />
          {errors.descripcion && <ErrorMessage>{errors.descripcion.message}</ErrorMessage>}
        </div>

        <div className="md:col-span-2 flex flex-col gap-2">
          <label htmlFor="preparacion" className="font-medium text-blue-900">
            Preparación
          </label>
          <textarea
            id="preparacion"
            rows={6}
            className="rounded-xl border bg-white border-blue-200 px-4 py-2 shadow-sm resize-y"
            placeholder="Mezclar ingredientes, hornear por 40 minutos."
            {...register("preparacion")}
          ></textarea>
          {errors.preparacion && <ErrorMessage>{errors.preparacion.message}</ErrorMessage>}
        </div>

        <div className="flex flex-col gap-2">
          <label htmlFor="ingredientes" className="font-medium text-blue-900">
            Ingredientes
          </label>
          <input
            type="text"
            id="ingredientes"
            className="rounded-xl border border-blue-200 bg-white px-4 py-2 shadow-sm"
            placeholder="Manzanas, harina, azúcar, mantequilla"
            {...register("ingredientes")}
          />
          {errors.ingredientes && <ErrorMessage>{errors.ingredientes.message}</ErrorMessage>}
        </div>

        <div className="flex flex-col gap-2">
          <label className="font-medium text-blue-900">Imagen de portada</label>
          <div className="flex items-center gap-4">
            <div className="w-16 h-16 bg-gray-200 rounded-xl flex items-center justify-center">📷</div>
            <div className="flex-1">
              <input
                type="file"
                accept="image/*"
                onChange={handleFileChange}
                className="hidden"
                id="image"
              />
              <label
                htmlFor="image"
                className="cursor-pointer rounded-md border border-green-500 px-4 py-2 text-green-600 hover:bg-green-100"
              >
                Elija archivo
              </label>
              <p className="text-sm mt-1 text-gray-600">{fileName}</p>
            </div>
          </div>
        </div>

        <div className="md:col-span-2">
          <button
            type="submit"
            className="bg-[#0A4486] text-white px-6 py-2 rounded-md hover:bg-[#1559A5] cursor-pointer 
            transition-colors duration-200"
            disabled={updateRecipeWithImageMutation.isPending}
          >
            {updateRecipeWithImageMutation.isPending
            ? "Actualizando..."
            : "+ Actualizar receta"}
          </button>
        </div>
      </form>
    </div>
  );
}