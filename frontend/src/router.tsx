import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomeLayout from "./layouts/HomeLayout";
import Home from "./view/home-page/Home";
import CardList from "./view/cardlist - page/CardList";
import RecipeLayout from "./layouts/RecipeLayout";
import RecipeDetailPage from "./view/recipeDetail - page/RecipeDetailPage";
import AuthLayout from "./layouts/AuthLayout";
import LoginPage from "./view/login - page/LoginPage";
import RegisterPage from "./view/register - page/RegisterPage";
import DashboardLayout from "./layouts/DashboardLayout";
import UploadRecipe from "./view/dashboard/subirReceta - page/UploadRecipe";
import RecipeList from "./view/dashboard/recipeList - page/RecipeList";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<HomeLayout />}>
          <Route path="/" element={<Home />} index />
          <Route path="/recetas" element={<CardList />} />
        </Route>
        <Route  element={<RecipeLayout />}>
          <Route path="/:id/receta-detalle" element={<RecipeDetailPage />} />
        </Route>
        <Route element={<AuthLayout />}>
          <Route path="/auth/login" element={<LoginPage />} />
          <Route path="/auth/register" element={<RegisterPage /> } />
        </Route>
        <Route element={<DashboardLayout />}>
          <Route path="/dashboard/subir-receta" element={<UploadRecipe />} />
          <Route path="/dashboard/recetas" element={<RecipeList />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}


// export const router = createBrowserRouter([
//   {
//     path: '/',
//     element: <HomeLayout />,
//     children: [
//       {
//         index: true,
//         element: <Home />
//       },
//       {
//         path: '/recetas',
//         element: <CardList />
//       }
//     ]
//   },
//   {
//     path: '/receta-detalle',
//     element: <RecipeLayout />,
//     children: [
//       {
//         index: true,
//         element: <RecipeDetailPage />
//       }
//     ]
//   },
//   {
//     path: "/auth",
//     element: <AuthLayout />,
//     children: [
//       {
//         path: 'login',
//         index: true,
//         element: <LoginPage />
//       },
//       {
//         path: 'register',
//         element: <RegisterPage />
//       }
//     ]
//   },
//   {
//     path: '/dashboard',
//     element: <DashboardLayout />,
//     children: [
//       {
//         path: 'subir-receta',
//         index: true,
//         element: <UploadRecipe />
//       },
//       {
//         path: 'recetas',
//         element: <RecipeList />
//       }
//     ]
//   }
// ])