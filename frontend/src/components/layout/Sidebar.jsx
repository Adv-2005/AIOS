import { NavLink } from "react-router-dom";

const links = [
  {
    name: "Dashboard",
    path: "/",
  },
  {
    name: "Company Brain",
    path: "/company-brain",
  },
  {
    name: "Project Planner",
    path: "/project-planner",
  },
  {
    name: "Productivity",
    path: "/productivity",
  },
  {
    name: "Monday Session",
    path: "/monday-session",
  },
  {
    name: "KPI Dashboard",
    path: "/kpi-dashboard",
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white flex flex-col">
      <div className="text-2xl font-bold p-6 border-b border-slate-700">
        AI COO
      </div>

      <nav className="flex-1 p-4 space-y-2">
        {links.map((link) => (
          <NavLink
            key={link.path}
            to={link.path}
            className={({ isActive }) =>
              `block rounded-lg px-4 py-3 transition ${
                isActive
                  ? "bg-blue-600"
                  : "hover:bg-slate-800"
              }`
            }
          >
            {link.name}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}