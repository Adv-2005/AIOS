import api from "./axios";

export async function generateMondaySession() {
  const response = await api.post(
    "/strategy/monday-session",
    {}
  );

  return response.data;
}