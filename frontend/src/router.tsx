import { createBrowserRouter } from "react-router-dom";
import HomeLayout from "./layouts/HomeLayout";
import Home from "./view/home-page/Home";
import CardList from "./view/cardlist - page/CardList";


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
  }
])