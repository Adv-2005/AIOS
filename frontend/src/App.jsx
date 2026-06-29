import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "./components/layout/MainLayout";

import Dashboard from "./pages/Dashboard";
import CompanyBrain from "./pages/CompanyBrain";
import ProjectPlanner from "./pages/ProjectPlanner";
import Productivity from "./pages/Productivity";
import MondaySession from "./pages/MondaySession";
import KPIDashboard from "./pages/KPIDashboard";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/company-brain" element={<CompanyBrain />} />
          <Route path="/project-planner" element={<ProjectPlanner />} />
          <Route path="/productivity" element={<Productivity />} />
          <Route path="/monday-session" element={<MondaySession />} />
          <Route path="/kpi-dashboard" element={<KPIDashboard />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;