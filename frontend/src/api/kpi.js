import api from "./axios";

export async function getDashboard() {

    const response = await api.get("/kpi/dashboard");

    return response.data;
}