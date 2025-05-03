import { Outlet } from "react-router-dom";

export default function AuthLayout() {
  return (
    <div className="min-h-screen bg-[#0A2B74] flex items-center justify-center p-4">
      <div className="bg-white rounded-md p-8 w-full max-w-md shadow-md">
        <Outlet />
      </div>
    </div>
  );
}
