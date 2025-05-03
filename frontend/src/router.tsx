import { createBrowserRouter } from "react-router-dom";
import HomeLayout from "./layouts/HomeLayout";
import Home from "./view/home-page/Home";
import CardList from "./view/cardlist - page/CardList";
import RecipeLayout from "./layouts/RecipeLayout";
import RecipeDetailPage from "./view/recipeDetail - page/RecipeDetailPage";
import AuthLayout from "./layouts/AuthLayout";
import LoginPage from "./view/login - page/LoginPage";
import RegisterPage from "./view/register - page/RegisterPage";


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
  },
  {
    path: "/auth",
    element: <AuthLayout />,
    children: [
      {
        path: 'login',
        element: <LoginPage />
      },
      {
        path: 'register',
        element: <RegisterPage />
      }
    ]
  }
])