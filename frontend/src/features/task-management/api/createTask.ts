import { httpClient } from "@/api/http"

export interface CreateTaskDTO {
    title: string
    description?: string
    deadline?: string // YYYY-MM-DD
}

export interface Task {
    id: number
    title: string
    description?: string
    deadline?: string
    status: "PENDING" | "COMPLETED"
    created_at: string
}

export const createTask = async (data: CreateTaskDTO): Promise<Task> => {
    const response = await httpClient.post<Task>("/tasks/", data)
    return response.data
}
