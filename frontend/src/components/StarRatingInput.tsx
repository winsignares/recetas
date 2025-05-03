import { useState } from 'react';

type StartRatingInputProps = {
  rating: number;
  onChange: (value: number) => void;
}

export default function StarRatingInput({ rating, onChange } : StartRatingInputProps) {
  const [hovered, setHovered] = useState(0);

  return (
    <div className="flex space-x-1 text-2xl cursor-pointer text-yellow-500">
      {[1, 2, 3, 4, 5].map((star) => (
        <span
          key={star}
          onClick={() => onChange(star)}
          onMouseEnter={() => setHovered(star)}
          onMouseLeave={() => setHovered(0)}
        >
          {star <= (hovered || rating) ? '★' : '☆'}
        </span>
      ))}
    </div>
  );
}
