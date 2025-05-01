import { createBrowserRouter } from "react-router-dom";
import HomeLayout from "./layouts/HomeLayout";
import Home from "./view/home-page/Home";
import CardList from "./view/cardlist - page/CardList";
import RecipeLayout from "./layouts/RecipeLayout";
import RecipeDetailPage from "./view/recipeDetail - page/RecipeDetailPage";


export const router = createBrowserRouter([
  {
    path: '/',
    element: <HomeLayout />,
    children: [
      {
        index: true,
        element: <Home />
      },
      {
        path: '/recetas',
        element: <CardList />
      }
    ]
  },
  {
    path: '/receta-detalle',
    element: <RecipeLayout />,
    children: [
      {
        index: true,
        element: <RecipeDetailPage />
      }
    ]
  }
])