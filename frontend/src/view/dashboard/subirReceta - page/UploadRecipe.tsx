import ErrorMessage from "@/components/ErrorMessage";
import { FormReceta, formRecetaSchema } from "@/types";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
import { createImage, createRecipe, createRecipeWithImage } from "@/api/recipeApi";

export default function UploadRecipe() {
  const [file, setFile] = useState<File | null>(null);
  const [fileName, setFileName] = useState("Ningún archivo elegido");

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset
  } = useForm<FormReceta>({
    resolver: zodResolver(formRecetaSchema),
    defaultValues: {
      titulo: "",
      descripcion: "",
      ingredientes: "",
      preparacion: "",
    },
  });

  const createRecipeWithImageMutation = useMutation({
    mutationFn: ({ formData, image }: { formData: FormReceta; image: File }) =>
      createRecipeWithImage(formData, image),
  });

  const createRecipeMutation = useMutation({
    mutationFn: createRecipe,
  });

  const uploadImageMutation = useMutation({
    mutationFn: ({ image, receta_id }: { image: File; receta_id: number }) =>
      createImage(image, receta_id),
  });

  const onSubmit = async (formValues: FormReceta) => {
    try {
      if (!file) {
        alert("Por favor, selecciona una imagen ❗");
        return;
      }
  
      const receta = await createRecipeWithImageMutation.mutateAsync({
        formData: formValues,
        image: file,
      });
  
      alert("Receta e imagen guardadas exitosamente ✅");
      reset();
      setFile(null);
      setFileName("Ningún archivo elegido");
    } catch (error) {
      console.error("Error al subir receta o imagen:", error);
      alert("Error al subir la receta");
    }
  };

  // const onSubmit = async (formValues: FormReceta) => {
  //   try {
  //     const receta = await createRecipeMutation.mutateAsync(formValues);

  //     if (receta?.id && file) {
  //       await uploadImageMutation.mutateAsync({
  //         image: file,
  //         receta_id: receta.id,
  //       });
  //       alert("Receta e imagen guardadas exitosamente ✅");
  //       reset()
  //     } else {
  //       alert("Todos los campos son necesarios❗");
  //     }
  //   } catch (error) {
  //     console.error("Error al subir receta o imagen:", error);
  //     alert("Error al subir la receta");
  //   }
  // };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setFileName(e.target.files[0].name);
    } else {
      setFile(null);
      setFileName("Ningún archivo elegido");
    }
  };

  return (
    <div className="min-h-screen w-full p-4 md:p-8 shadow-md">
      <h2 className="text-3xl font-bold text-[#0A4486]">Subir Nueva Receta</h2>
      <p>Sube la receta que creas necesaria para compartir</p>

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
            disabled={createRecipeMutation.isPending || uploadImageMutation.isPending}
          >
            {createRecipeMutation.isPending || uploadImageMutation.isPending
            ? "Subiendo..."
            : "+ Subir nueva receta"}
          </button>
        </div>
      </form>
    </div>
  );
}
