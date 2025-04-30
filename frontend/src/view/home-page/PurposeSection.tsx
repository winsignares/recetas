import { Link } from "react-router-dom";


export default function PurposeSection() {
  return (
    <section className="text-gray-600 bg-[#0A4486]">
      <div className="container px-5 py-24 mx-auto flex flex-wrap">
        <h2 className="sm:text-3xl text-2xl text-white font-medium title-font mb-2 md:w-2/5">
          Una comunidad para amantes de la cocina
        </h2>
        <div className="md:w-3/5 md:pl-6">
          <p className="leading-relaxed text-base text-gray-300">
            Nuestra misión es conectar personas a través de la comida. Aquí puedes compartir tus platos favoritos, inspirarte con nuevas recetas y crear momentos únicos en la cocina.
          </p>
          <div className="flex md:mt-4 mt-6">
            <Link to={'/recetas'} className="inline-flex text-black font-bold bg-white border-0 py-1 
              px-4 focus:outline-none hover:bg-gray-100 rounded transition-colors duration-200"
            >
              Explorar Recetas
            </Link>
          </div>
        </div>
      </div>
    </section>
  )
}
