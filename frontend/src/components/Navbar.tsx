import { useState } from "react"
import { MdMenu, MdClose } from "react-icons/md"
import { Link } from "react-router-dom";

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen)
  }

  return (
    <div className="bg-white sticky top-0 left-0 right-0 z-[999999]">
      <div className="max-w-screen-2xl m-auto py-4 px-5 flex justify-between items-center">
        {/* logo */}
        <a href="/">
          <img src="/logo.png" alt="Logo" className="w-28" />
        </a>

        {/* Menu for small devices */}
        <div className="lg:hidden">
          <button onClick={toggleMenu}>
            {isMenuOpen ? (
              <MdClose className="text-2xl text-[#0A4486]" />
            ): (
              <MdMenu className="text-2xl text-[#0A4486]" />
            )}
          </button>
        </div>
        
        {/* Menu for large devices */}
        <div className="hidden lg:block">
          <nav>
            <ul className="flex items-center gap-6">
              <li>
                <Link
                  to="/"
                  className="uppercase font-semibold hover:text-[#0A4486]"
                >
                  Inicio
                </Link>
              </li>
              <li>
                <Link
                  to="/recetas"
                  className="uppercase font-semibold hover:text-[#0A4486]"
                >
                  Ver Recetas
                </Link>
              </li>
            </ul>
          </nav>
        </div>

        <div className="hidden lg:flex gap-2">
          <Link to={'/auth/login'} className="px-2 py-2 bg-[#0A4486] text-white cursor-pointer
            hover:bg-[#1559A5] hover:text-white rounded transition-colors duration-200 font-bold"
          >
            Iniciar Sesión
          </Link>
        </div>

        {/* Mobile menu */}
        {isMenuOpen && (
          <div className="fixed inset-0 bg-white z-50 shadow-md lg:hidden">
            <div className="flex justify-between items-center p-4 border-b border-b-gray-300">
              <div>
                <img src="/logo.png" alt="Logo" className="w-28" />
              </div>

              <button onClick={toggleMenu}>
                <MdClose className="text-2xl text-[#0A4486]"/>
              </button>
            </div>

            <nav className="mt-4">
              <ul className="flex flex-col gap-6 text-center">
                <li>
                  <Link
                    to="/"
                    className="uppercase font-semibold"
                    onClick={toggleMenu}
                  >
                    Inicio
                  </Link>
                </li>
                <li>
                  <Link
                    to="/recetas"
                    className="uppercase font-semibold"
                    onClick={toggleMenu}
                  >
                    Ver Recetas
                  </Link>
                </li>
              </ul>
            </nav>

            <div className="mt-6 text-center flex flex-col gap-2 px-20">
              <Link to="/auth/login" className="px-2 py-2 bg-[#0A4486] text-white cursor-pointer
              hover:bg-[#1559A5] hover:text-white rounded transition-colors duration-200 font-bold"
              >
                Iniciar Sesión
              </Link>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
