import { Link } from 'react-router-dom'

export default function InvitationToRegistration() {
  return (
    <section className="text-gray-600 body-font bg-gray-100">
      <div className="container px-5 py-24 mx-auto">
        <div className="lg:w-2/3 flex flex-col sm:flex-row sm:items-center items-start mx-auto">
          <h1 className="flex-grow sm:pr-16 text-2xl font-bold title-font text-gray-900">
            Únete a nuestra comunidad de cocineros. Comparte tus recetas, guarda tus favoritas y
            descubre nuevos sabores cada día.
          </h1>
          <Link to="/registro" className="flex-shrink-0 text-white bg-[#0A4486] border-0 py-2 
            px-8 focus:outline-none hover:bg-[#1559A5] rounded font-bold text-lg mt-10 sm:mt-0
            transition-colors duration-200"
          >
            Crear cuenta
          </Link>
        </div>
      </div>
    </section>
  )
}
