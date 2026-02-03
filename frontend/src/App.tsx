import { Routes, Route, Navigate } from "react-router-dom"
import { CreateTaskPage } from "./features/task-management/pages/CreateTaskPage"

function App() {
  return (
    <div className="min-h-screen bg-background font-sans antialiased">
      <Routes>
        <Route path="/" element={<Navigate to="/tasks/new" replace />} />
        <Route path="/tasks/new" element={<CreateTaskPage />} />
      </Routes>
    </div>
  )
}

export default App
