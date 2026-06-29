import { useState } from "react";
import { generateMondaySession } from "../api/strategy";

export default function MondaySession() {
  const [report, setReport] = useState(null);

  const [loading, setLoading] = useState(false);

  async function handleGenerate() {
    setLoading(true);

    try {
      const data = await generateMondaySession();

      setReport(data);
    } catch (err) {
      console.error(err);
      alert("Failed to generate Monday Session.");
    }

    setLoading(false);
  }

  return (
    <div className="space-y-6">

      <h1 className="text-3xl font-bold">
        Monday Session Generator
      </h1>

      <button
        onClick={handleGenerate}
        className="border rounded px-4 py-2"
      >
        {loading ? "Generating..." : "Generate Report"}
      </button>

      {report && (

        <>

          {/* Executive Summary */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-3">
              Executive Summary
            </h2>

            <p>{report.executive_summary}</p>

          </section>

          {/* Projects at Risk */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-3">
              Projects at Risk
            </h2>

            {report.projects_at_risk.length === 0 ? (
              <p>No projects at risk.</p>
            ) : (
              report.projects_at_risk.map((project, index) => (
                <div
                  key={index}
                  className="border-b py-3"
                >
                  <strong>{project.project}</strong>

                  <p>{project.reason}</p>
                </div>
              ))
            )}

          </section>

          {/* High Priority Work */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-3">
              High Priority Work
            </h2>

            {report.high_priority_work.map((task, index) => (

              <div
                key={index}
                className="border-b py-3"
              >

                <strong>{task.task}</strong>

                <p>{task.reason}</p>

              </div>

            ))}

          </section>

          {/* Key Risks */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-3">
              Key Risks
            </h2>

            <ul className="list-disc ml-6 space-y-2">

              {report.key_risks.map((risk, index) => (

                <li key={index}>
                  {risk}
                </li>

              ))}

            </ul>

          </section>

          {/* Recommendations */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-3">
              Recommendations
            </h2>

            <ul className="list-disc ml-6 space-y-2">

              {report.recommendations.map((recommendation, index) => (

                <li key={index}>
                  {recommendation}
                </li>

              ))}

            </ul>

          </section>

          {/* Next Week Priorities */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-3">
              Next Week Priorities
            </h2>

            <ul className="list-disc ml-6 space-y-2">

              {report.next_week_priorities.map((priority, index) => (

                <li key={index}>
                  {priority}
                </li>

              ))}

            </ul>

          </section>

          {/* Industry Updates */}

          <section className="border rounded p-4 bg-white">

            <h2 className="text-xl font-semibold mb-3">
              Industry Updates
            </h2>

            {report.industry_updates.map((update, index) => (

              <div
                key={index}
                className="border-b py-4"
              >

                <strong>{update.title}</strong>

                <p className="mt-2">

                  {update.summary}

                </p>

                <p className="mt-2">

                  <strong>Business Impact:</strong>{" "}

                  {update.business_impact}

                </p>

              </div>

            ))}

          </section>

        </>

      )}

    </div>
  );
}