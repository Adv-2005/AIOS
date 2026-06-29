import { Link } from "react-router-dom";

const modules = [
  {
    title: "Company Brain",
    description:
      "Upload company documents and ask questions using AI.",
    path: "/company-brain",
  },
  {
    title: "Project Planner",
    description:
      "Generate implementation plans from requirement documents.",
    path: "/project-planner",
  },
  {
    title: "Employee Productivity",
    description:
      "Generate AI-powered daily work plans for different roles.",
    path: "/productivity",
  },
  {
    title: "Monday Session",
    description:
      "Generate executive weekly strategy reports.",
    path: "/monday-session",
  },
  {
    title: "KPI Dashboard",
    description:
      "Monitor projects, tasks and organization metrics.",
    path: "/kpi-dashboard",
  },
];

export default function Dashboard() {
  return (
    <div className="space-y-8">

      <div>

        <h1 className="text-4xl font-bold">
          AI Operations Command Centre
        </h1>

        <p className="mt-3">
          Welcome to your AI-powered operations platform.
        </p>

      </div>

      <div className="grid gap-6">

        {modules.map((module) => (

          <div
            key={module.title}
            className="border rounded p-5 bg-white"
          >

            <h2 className="text-2xl font-semibold">

              {module.title}

            </h2>

            <p className="my-3">

              {module.description}

            </p>

            <Link
              to={module.path}
              className="border rounded px-4 py-2 inline-block"
            >
              Open
            </Link>

          </div>

        ))}

      </div>

    </div>
  );
}