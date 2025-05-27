import { deleteComment } from "@/api/recipeApi";
import { Receta } from "@/types";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { X } from "lucide-react";

type ReviewListProps = {
  data: Receta;
};

export default function ReviewList({ data }: ReviewListProps) {
  const queryClient = useQueryClient()

  const { mutate, isPending } = useMutation({
    mutationFn: (comentarioId: number) => deleteComment(comentarioId),
    onSuccess: () => {
      queryClient.invalidateQueries({queryKey: ['recipeDetail']})
    }
  })

  const handleDelete = (comentarioId: number) => {
    mutate(comentarioId)
  };

  return (
    <section className="mt-10">
      <h2 className="text-xl font-semibold mb-6">Valoraciones</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {data.comentarios.map((comentario) => (
          <div key={comentario.id} className="flex gap-4 items-center">
            <div className="w-10 h-10 rounded-full bg-gray-300 mt-1" />
            <div className="flex-1 relative">
              <p className="text-gray-700 text-sm pr-6">{comentario.contenido}</p>
              <button
                onClick={() => handleDelete(comentario.id)}
                className="absolute top-0 right-0 text-gray-400 hover:text-red-500 cursor-pointer"
                aria-label="Eliminar comentario"
                disabled={isPending}
              >
                <X size={16} />
              </button>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
