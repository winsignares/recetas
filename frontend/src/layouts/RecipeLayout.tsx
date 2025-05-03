import Navbar from '../components/Navbar';
import { Outlet } from 'react-router-dom';

export default function RecipeLayout() {
  return (
    <div>
      <Navbar />
      <main className="max-w-5xl mx-auto px-4 py-8">
        <Outlet />
      </main>
    </div>
  );
}
