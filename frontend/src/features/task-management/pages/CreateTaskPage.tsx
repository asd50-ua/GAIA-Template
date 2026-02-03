import { useMutation } from "@tanstack/react-query"
// import { useNavigate } from "react-router-dom"
import { type CreateTaskDTO, createTask } from "../api/createTask"
import { CreateTaskForm } from "../components/CreateTaskForm"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export function CreateTaskPage() {
    // const navigate = useNavigate()

    const mutation = useMutation({
        mutationFn: createTask,
        onSuccess: () => {
            // Navigate or show success
            // Since we don't have list page yet, just alert or console
            alert("Task created!")
            // navigate("/") 
        },
        onError: (error) => {
            console.error("Failed to create task", error)
            alert("Failed to create task")
        }
    })

    const handleSubmit = (data: CreateTaskDTO) => {
        mutation.mutate(data)
    }

    return (
        <div className="container mx-auto py-10 max-w-lg">
            <Card>
                <CardHeader>
                    <CardTitle>Create New Task</CardTitle>
                    <CardDescription>Add a new task to your list.</CardDescription>
                </CardHeader>
                <CardContent>
                    <CreateTaskForm onSubmit={handleSubmit} isLoading={mutation.isPending} />
                </CardContent>
            </Card>
        </div>
    )
}
