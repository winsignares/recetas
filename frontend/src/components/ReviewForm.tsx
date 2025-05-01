export default function ReviewForm() {
  return (
    <section className="mt-12 border-t pt-8">
      <h2 className="text-lg font-semibold mb-2">Añade una valoración</h2>
      <p className="text-sm text-gray-600 mb-4">
        Tu dirección de correo electrónico no será publicada.
      </p>

      <form className="space-y-6">
        <div>
          <label className="block font-medium">Tu puntuación:</label>
          <div className="text-xl text-yellow-500">☆☆☆☆☆</div>
        </div>

        <div>
          <label className="block font-medium">Tu valoración:</label>
          <textarea className="w-full p-3 border rounded-lg" rows={5} />
        </div>

        <div className="grid md:grid-cols-2 gap-4">
          <input className="p-3 border rounded-lg w-full" placeholder="Nombre" />
          <input className="p-3 border rounded-lg w-full" placeholder="Correo electrónico" />
        </div>

        <button className="bg-blue-700 text-white px-6 py-2 rounded-lg hover:bg-blue-800">
          Enviar
        </button>
      </form>
    </section>
  );
}
