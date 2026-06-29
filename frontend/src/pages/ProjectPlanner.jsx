import { useState } from "react";
import { uploadRequirement } from "../api/project";

export default function ProjectPlanner() {

  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [plan, setPlan] = useState(null);

  async function handleGenerate() {

    if (!file) return;

    setLoading(true);

    try {

      const data = await uploadRequirement(file);

      setPlan(data);

    } catch (err) {

      console.error(err);

      alert("Failed to generate project.");

    }

    setLoading(false);

  }

  return (

    <div className="space-y-6">

      <h1 className="text-3xl font-bold">

        Project Planner

      </h1>

      <div className="border rounded p-4 bg-white">

        <input

          type="file"

          accept=".pdf"

          onChange={(e) => setFile(e.target.files[0])}

        />

        <button

          className="border rounded px-4 py-2 ml-4"

          onClick={handleGenerate}

        >

          {loading ? "Generating..." : "Generate Project"}

        </button>

      </div>

      {plan && (

        <div className="space-y-6">

    <section className="border rounded p-4 bg-white">
      <h2 className="text-2xl font-semibold">
        {plan.project_plan.project_name}
      </h2>

      <p className="mt-3">
        {plan.project_plan.summary}
      </p>

      <div className="mt-4">
        <p>
          <strong>Project ID:</strong> {plan.project_id}
        </p>

        <p>
          <strong>Tasks Created:</strong> {plan.tasks_created}
        </p>

        <p>
          <strong>Milestones:</strong> {plan.milestones_created}
        </p>
      </div>
    </section>

    <section className="border rounded p-4 bg-white">

      <h2 className="text-xl font-semibold mb-4">
        Milestones
      </h2>

      <ul className="space-y-3">

        {plan.project_plan.milestones.map((milestone, index) => (

          <li key={index}>

            <strong>{milestone.name}</strong>

            <p>{milestone.description}</p>

          </li>

        ))}

      </ul>

    </section>

        <section className="border rounded p-4 bg-white">

      <h2 className="text-xl font-semibold mb-4">
        Tasks
      </h2>

      <table className="w-full border-collapse">

        <thead>

          <tr className="border-b">

            <th className="text-left p-2">Task</th>

            <th className="text-left p-2">Priority</th>

            <th className="text-left p-2">Hours</th>

            <th className="text-left p-2">Role</th>

            <th className="text-left p-2">Dependencies</th>

          </tr>

        </thead>

        <tbody>

          {plan.project_plan.tasks.map((task) => (

            <tr
              key={task.task_id}
              className="border-b"
            >

              <td className="p-2">
                {task.title}
              </td>

              <td className="p-2">
                {task.priority}
              </td>

              <td className="p-2">
                {task.estimated_hours}
              </td>

              <td className="p-2">
                {task.suggested_role}
              </td>

              <td className="p-2">

                {task.depends_on.length > 0
                  ? task.depends_on.join(", ")
                  : "-"}

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </section>

        <section className="border rounded p-4 bg-white">

      <h2 className="text-xl font-semibold mb-4">
        Risks
      </h2>

      <ul className="list-disc ml-6 space-y-2">

        {plan.project_plan.risks.map((risk, index) => (

          <li key={index}>
            {risk}
          </li>

        ))}

      </ul>

    </section>

  </div>
)}


    </div>

  );

}