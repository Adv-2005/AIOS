import { useEffect, useState } from "react";
import { getDashboard } from "../api/kpi";

export default function KPIDashboard() {
  const [dashboard, setDashboard] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadDashboard() {
      try {
        const data = await getDashboard();
        setDashboard(data);
      } catch (err) {
        console.error(err);
        setError("Failed to load dashboard.");
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  if (loading) return <h2>Loading...</h2>;

  if (error) return <h2>{error}</h2>;

  return (
    <div className="space-y-8">

      <h1 className="text-3xl font-bold">
        KPI Dashboard
      </h1>

      {/* Projects */}

      <section className="border rounded p-4 bg-white">
        <h2 className="text-xl font-semibold mb-2">Projects</h2>

        <p>Total Projects: {dashboard.overview.total_projects}</p>
        <p>Active Projects: {dashboard.overview.active_projects}</p>
        <p>Completed Projects: {dashboard.overview.completed_projects}</p>
        <p>
          Completion:{" "}
          {dashboard.overview.project_completion_percentage}%
        </p>
      </section>

      {/* Tasks */}

      <section className="border rounded p-4 bg-white">
        <h2 className="text-xl font-semibold mb-2">Tasks</h2>

        <p>Total Tasks: {dashboard.tasks.total_tasks}</p>
        <p>Completed: {dashboard.tasks.completed_tasks}</p>
        <p>In Progress: {dashboard.tasks.in_progress_tasks}</p>
        <p>Pending: {dashboard.tasks.pending_tasks}</p>
      </section>

      {/* Priorities */}

      <section className="border rounded p-4 bg-white">
        <h2 className="text-xl font-semibold mb-2">
          Priority Breakdown
        </h2>

        <p>High: {dashboard.priorities.high}</p>
        <p>Medium: {dashboard.priorities.medium}</p>
        <p>Low: {dashboard.priorities.low}</p>
      </section>

      {/* Blocked */}

      <section className="border rounded p-4 bg-white">
        <h2 className="text-xl font-semibold mb-2">
          Blocked Tasks
        </h2>

        <p>{dashboard.blocked_tasks}</p>
      </section>

      {/* Productivity */}

      <section className="border rounded p-4 bg-white">
        <h2 className="text-xl font-semibold mb-2">
          Team Productivity
        </h2>

        {dashboard.team_productivity.map((team) => (
          <div
            key={team.team}
            className="flex justify-between border-b py-2"
          >
            <span>{team.team}</span>

            <span>{team.productivity}%</span>
          </div>
        ))}
      </section>

      {/* Trend */}

      <section className="border rounded p-4 bg-white">
        <h2 className="text-xl font-semibold mb-2">
          Weekly Trend
        </h2>

        {dashboard.trend.map((week) => (
          <div
            key={week.week}
            className="flex justify-between border-b py-2"
          >
            <span>{week.week}</span>

            <span>{week.completion}%</span>
          </div>
        ))}
      </section>

    </div>
  );
}