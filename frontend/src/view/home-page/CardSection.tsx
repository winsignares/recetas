import desayunoImg from "../../assets/desayuno-card.jpg"
import almuerzoImg from "../../assets/almuerzo-card.jpg"
import cenaImg from "../../assets/cena-card.jpg"
import postreImg from "../../assets/postre-card.jpg"

export default function CardSection() {
  return (
    <section className="text-gray-600 body-font">
      <div className="container px-5 py-24 mx-auto">
        <div className="flex flex-wrap w-full mb-20">
          <div className="lg:w-1/2 w-full mb-6 lg:mb-0">
            <h2 className="sm:text-3xl text-2xl font-bold title-font mb-2 text-gray-900">¿Sin saber qué cocinar?</h2>
            <div className="h-1 w-20 bg-[#0A4486] rounded"></div>
          </div>
          <p className="lg:w-1/2 w-full leading-relaxed text-gray-500">Cocinar no tiene que ser complicado. Comparte momentos, sabores y tradiciones con cada receta. Nuestra colección está pensada para ayudarte a disfrutar el arte de cocinar sin estrés.</p>
        </div>
        <div className="flex flex-wrap -m-4 items-stretch">
          <div className="xl:w-1/4 md:w-1/2 p-4">
            <div className="bg-gray-100 p-6 rounded-lg h-full flex flex-col">
              <img className="h-60 rounded w-full object-cover object-center mb-6" src={ desayunoImg } alt="Desayuno image" />
              <h2 className="text-lg text-gray-900 font-bold title-font mb-4">Energía para comenzar el día</h2>
              <p className="leading-relaxed text-base">Descubre recetas fáciles y nutritivas para empezar tus mañanas con buen sabor. ¡Desde pancakes hasta bowls energéticos!</p>
            </div>
          </div>
          <div className="xl:w-1/4 md:w-1/2 p-4">
            <div className="bg-gray-100 p-6 rounded-lg h-full flex flex-col">
              <img className="h-60 rounded w-full object-cover object-center mb-6" src={ almuerzoImg } alt="Almuerzo image" />
              <h2 className="text-lg text-gray-900 font-bold title-font mb-4">Recetas para el mediodía</h2>
              <p className="leading-relaxed text-base">Ideas rápidas y deliciosas para el almuerzo. Recetas caseras, saludables y listas en menos de 30 minutos.</p>
            </div>
          </div>
          <div className="xl:w-1/4 md:w-1/2 p-4">
            <div className="bg-gray-100 p-6 rounded-lg h-full flex flex-col">
              <img className="h-60 rounded w-full object-cover object-center mb-6" src={ cenaImg } alt="Cena image" />
              <h2 className="text-lg text-gray-900 font-bold title-font mb-4">Cenas ligeras o contundentes</h2>
              <p className="leading-relaxed text-base">¿Cenas rápidas después del trabajo? ¿O algo especial para compartir? Encuentra la receta perfecta para cerrar el día.</p>
            </div>
          </div>
          <div className="xl:w-1/4 md:w-1/2 p-4">
            <div className="bg-gray-100 p-6 rounded-lg h-full flex flex-col">
              <img className="h-60 rounded w-full object-cover object-center mb-6" src={ postreImg } alt="Postre image" />
              <h2 className="text-lg text-gray-900 font-bold title-font mb-4">Dulces momentos</h2>
              <p className="leading-relaxed text-base">Desde clásicos como flan y brownies hasta opciones sin azúcar. Inspírate con recetas irresistibles para endulzar la vida.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
