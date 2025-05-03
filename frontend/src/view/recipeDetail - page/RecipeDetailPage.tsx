
import ReviewList from '../../components/ReviewList';
import ReviewForm from '../../components/ReviewForm';
import RecipeDetail from '../../components/RecipeDetail';

export default function RecipeDetailPage() {
  return (
    <>
      <div className='mt-10'>
        <RecipeDetail />
        <ReviewList />
        <ReviewForm />
      </div>
    </>
  );
}
