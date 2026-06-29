import { useState } from "react";
import { generateProductivity } from "../api/productivity";

const ROLES = [
  "Backend Developer",
  "Frontend Developer",
  "Full Stack Developer",
  "AI/ML Engineer",
  "DevOps Engineer",
  "QA Engineer",
  "UI/UX Designer",
  "Product Manager",
];

export default function Productivity() {
  const [role, setRole] = useState(ROLES[0]);
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleGenerate() {
    setLoading(true);

    try {
      const data = await generateProductivity(role);
      setPlan(data);
    } catch (err) {
      console.error(err);
      alert("Failed to generate productivity plan.");
    }

    setLoading(false);
  }

  return (
    <div className="space-y-6">

      <h1 className="text-3xl font-bold">
        Employee Productivity
      </h1>

      <div className="border rounded p-4 bg-white">

        <label className="block mb-2 font-semibold">
          Select Role
        </label>

        <select
          value={role}
          onChange={(e) => setRole(e.target.value)}
          className="border rounded p-2"
        >
          {ROLES.map((r) => (
            <option key={r} value={r}>
              {r}
            </option>
          ))}
        </select>

        <button
          onClick={handleGenerate}
          className="border rounded px-4 py-2 ml-4"
        >
          {loading ? "Generating..." : "Generate Plan"}
        </button>

      </div>

      {plan && (

        <>

          {/* Summary */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-2">
              Summary
            </h2>

            <p>{plan.summary}</p>

            <p className="mt-4">
              <strong>Total Estimated Hours:</strong>{" "}
              {plan.total_hours}
            </p>

          </section>

          {/* Tasks */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-4">
              Today's Tasks
            </h2>

            {plan.tasks.length === 0 ? (

              <p>No active tasks.</p>

            ) : (

              <table className="w-full">

                <thead>

                  <tr className="border-b">

                    <th className="text-left p-2">Task</th>

                    <th className="text-left p-2">Reason</th>

                    <th className="text-left p-2">Hours</th>

                  </tr>

                </thead>

                <tbody>

                  {plan.tasks.map((task, index) => (

                    <tr
                      key={index}
                      className="border-b"
                    >

                      <td className="p-2">
                        {task.title}
                      </td>

                      <td className="p-2">
                        {task.reason}
                      </td>

                      <td className="p-2">
                        {task.estimated_hours}
                      </td>

                    </tr>

                  ))}

                </tbody>

              </table>

            )}

          </section>

          {/* Risks */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-4">
              Risks
            </h2>

            {plan.risks.length === 0 ? (

              <p>No risks identified.</p>

            ) : (

              <ul className="list-disc ml-6 space-y-2">

                {plan.risks.map((risk, index) => (

                  <li key={index}>
                    {risk}
                  </li>

                ))}

              </ul>

            )}

          </section>

        </>

      )}

    </div>
  );
}