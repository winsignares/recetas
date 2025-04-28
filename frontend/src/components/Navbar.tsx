import { useState } from "react"
import { MdMenu, MdClose } from "react-icons/md"

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
                <a href="/" className="uppercase font-semibold">Inicio</a>
              </li>
              <li>
                <a href="/recetas" className="uppercase font-semibold">Ver Recetas</a>
              </li>
            </ul>
          </nav>
        </div>

        <div className="hidden lg:flex gap-2">
          <a className="px-2 py-2 border-2 border-b-[#0A4486] cursor-pointer
            hover:bg-[#0A4486] hover:text-white rounded-md transition-colors duration-200"
          >
            Iniciar Sesión
          </a>

          <a className="px-2 py-2 bg-[#0A4486] text-white cursor-pointer
            hover:bg-[#1559A5] hover:text-white rounded-md transition-colors duration-200"
          >
            Registrarse
          </a>
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
                  <a href="/" className="uppercase font-semibold">Inicio</a>
                </li>
                <li>
                  <a href="/recetas" className="uppercase font-semibold">Ver Recetas</a>
                </li>
              </ul>
            </nav>

            <div className="mt-6 text-center flex flex-col gap-2 px-20">
              <a href="/" className="px-2 py-2 border-2 border-b-[#0A4486] cursor-pointer
              hover:bg-[#0A4486] hover:text-white rounded-md transition-colors duration-200"
              >
                Iniciar Sesión
              </a>
              <a href="/" className="px-2 py-2 bg-[#0A4486] text-white cursor-pointer
              hover:bg-[#1559A5] hover:text-white rounded-md transition-colors duration-200"
              >
                Registrarse
              </a>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
