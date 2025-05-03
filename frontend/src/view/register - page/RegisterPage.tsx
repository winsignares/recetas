import { useState } from "react";
import { Link, useLocation } from "react-router-dom";

export default function RegisterPage() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const location = useLocation();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log({ firstName, lastName, email, password });
  };

  const isLogin = location.pathname === "/auth/login";
  const isRegister = location.pathname === "/auth/register";

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="flex justify-center gap-4 text-[#0A2B74] font-bold text-lg">
        <Link
          to="/auth/login"
          className={`pb-1 hover:text-[#0A2B74] transition-colors duration-200 ${
            isLogin ? "border-b-2 border-[#0A2B74]" : "text-[#0A2B74]/60"
          }`}
        >
          Iniciar sesión
        </Link>
        <Link
          to="/auth/register"
          className={`pb-1 ${
            isRegister ? "border-b-2 border-[#0A2B74]" : "text-[#0A2B74]/60"
          }`}
        >
          Registrarse
        </Link>
      </div>

      <div>
        <label className="block text-sm mb-1 text-[#0A2B74]">Nombre</label>
        <input
          type="text"
          className="w-full px-3 py-2 border border-blue-100 rounded-md bg-blue-50 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          required
        />
      </div>

      <div>
        <label className="block text-sm mb-1 text-[#0A2B74]">Apellido</label>
        <input
          type="text"
          className="w-full px-3 py-2 border border-blue-100 rounded-md bg-blue-50 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          required
        />
      </div>

      <div>
        <label className="block text-sm mb-1 text-[#0A2B74]">Correo electrónico</label>
        <input
          type="email"
          className="w-full px-3 py-2 border border-blue-100 rounded-md bg-blue-50 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div>
        <label className="block text-sm mb-1 text-[#0A2B74]">Contraseña</label>
        <input
          type="password"
          className="w-full px-3 py-2 border border-blue-100 rounded-md bg-blue-50 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      <button
        type="submit"
        className="w-full py-2 bg-[#0A4486] hover:bg-[#1559A5] text-white 
        font-bold rounded-md cursor-pointer transition-colors duration-200"
      >
        Registrarse
      </button>
    </form>
  );
}
