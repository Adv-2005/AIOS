import api from "./axios";

export async function generateProductivity(role) {
  const response = await api.post("/productivity/generate", {
    role,
  });

  return response.data;
}