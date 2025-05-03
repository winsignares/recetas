const reviews = [
  {
    name: 'Persona 1',
    rating: 5,
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
  },
  {
    name: 'Persona 2',
    rating: 5,
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...',
  },
];

export default function ReviewList() {
  return (
    <section className="mt-10">
      <h2 className="text-xl font-semibold mb-6">2 valoraciones</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {reviews.map((review, idx) => (
          <div key={idx} className="flex gap-4 items-start">
            <div className="w-10 h-10 rounded-full bg-gray-300" />
            <div>
              <p className="font-bold">{review.name}</p>
              <p className="text-yellow-500 mb-2">{'★'.repeat(review.rating)}</p>
              <p className="text-gray-700 text-sm">{review.text}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
