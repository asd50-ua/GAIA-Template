import axios from "axios"

export const httpClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || "/api/v1",
    headers: {
        "Content-Type": "application/json",
    },
})

// Add interceptors for auth if needed later
httpClient.interceptors.response.use(
    (response) => response,
    (error) => {
        // Handle global errors like 401
        return Promise.reject(error)
    }
)
