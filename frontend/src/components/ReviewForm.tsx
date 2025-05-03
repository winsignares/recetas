import { FormEvent, useState } from 'react';
import StarRatingInput from './StarRatingInput';

export default function ReviewForm() {
  const [rating, setRating] = useState(0);
  const [comment, setComment] = useState('');

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('Calificación:', rating);
    console.log('Comentario:', comment);
  };

  return (
    <section className="mt-12 border-t pt-8">
      <h2 className="text-lg font-semibold mb-2">Añade una valoración</h2>
      <p className="text-sm text-gray-600 mb-4">
        Tu dirección de correo electrónico no será publicada.
      </p>

      <form
        className="space-y-6"
        onSubmit={handleSubmit}
      >
        <div>
          <label className="block font-medium">Tu puntuación:</label>
          <StarRatingInput rating={rating} onChange={setRating} />
        </div>

        <div>
          <label className="block font-medium">Tu valoración:</label>
          <textarea
            className="w-full p-3 border rounded-lg"
            rows={5}
            value={comment}
            onChange={(e) => setComment(e.target.value)}
          />
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
