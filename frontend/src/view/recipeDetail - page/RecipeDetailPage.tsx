
import ReviewList from '../../components/ReviewList';
import ReviewForm from '../../components/ReviewForm';
import RecipeDetail from '../../components/RecipeDetail';
import { useQuery } from '@tanstack/react-query';
import { getRecipeById } from '@/api/recipeApi';
import { useParams } from 'react-router-dom';

export default function RecipeDetailPage() {

  const { id } = useParams()
  const recipeId = id!

  const { data } = useQuery({
    queryKey: ['recipeDetail', recipeId],
    queryFn: () => getRecipeById(+recipeId)
  })

  if (data) return (
    <>
      <div className='mt-10'>
        <RecipeDetail data={data} />
        <ReviewList data={data} />
        <ReviewForm />
      </div>
    </>
  );
}
