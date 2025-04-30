import imgHeader from "../../assets/img-header.jpg"

export default function Header() {
  return (
    <section className="body-font bg-[#0A4486] mb-12">
      <div className="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center"
      >
        <div className="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left 
          mb-16 md:mb-0 items-center text-center"
        >
          <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-white">
            Descubre y comparte recetas deliciosas
            <br className="hidden lg:inline-block" />para cada ocasión 
          </h1>
          <p className="mb-8 leading-relaxed text-gray-300">
            Encuentra recetas caseras fáciles y sabrosas, comparte tus creaciones con la
            comunidad y recibe valoraciones de otros amantes de la cocina.
            Ideal para principiantes y chefs apasionados.
          </p>
        </div>
        <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
          <img className="object-cover object-center rounded shadow" alt="image header" src={ imgHeader } />
        </div>
      </div>
    </section>
  )
}
