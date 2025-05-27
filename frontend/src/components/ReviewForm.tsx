import { useForm } from 'react-hook-form'
import ErrorMessage from './ErrorMessage';
import { useParams } from 'react-router-dom';
import { Comment } from '@/types';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { createComment } from '@/api/recipeApi';

export default function ReviewForm() {
  const queryClient  = useQueryClient()

  const params = useParams()
  const recetaId = +params.id!

  const initialValues : Comment = {
    contenido: ""
  }
  
  const { register, handleSubmit, formState: { errors }, reset } = useForm({ defaultValues: initialValues })

  const { mutate } = useMutation({
    mutationFn: createComment,
    onError: () => {

    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['recipeDetail'] })
      reset()
    }
  })

  const handleForm = (commentFormData: Comment) => {
    const data = {
      commentFormData,
      receta_id: recetaId
    }
    mutate(data)
  }


  return (
    <section className="mt-12 border-t pt-8">
      <h2 className="text-lg font-semibold mb-2">Añade una valoración</h2>

      <form
        className="space-y-6"
        onSubmit={handleSubmit(handleForm)}
        noValidate
      >

        <div>
          <label htmlFor='contenido' className="block font-medium">Tu valoración:</label>
          <textarea
            id='contenido'
            className="w-full p-3 border rounded-lg"
            rows={5}
            {...register('contenido', {
              required: 'La valoración es obligatorio'
            })}
          />

          {errors.contenido && (
            <ErrorMessage>{ errors.contenido.message }</ErrorMessage>
          )}

        </div>

        <button
          className="bg-[#0A4486] text-white font-bold px-6 py-2 rounded-lg hover:bg-[#1559A5] 
            cursor-pointer transition-colors duration-200"
        >
          Enviar
        </button>
      </form>
    </section>
  );
}
