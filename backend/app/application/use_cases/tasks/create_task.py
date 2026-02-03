from app.domain.entities.task import Task
from app.domain.repositories.task_repository import TaskRepository
from typing import Optional
from datetime import date

class CreateTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def execute(self, title: str, user_id: int, description: Optional[str] = None, deadline: Optional[date] = None) -> Task:
        # Here we could add domain logic (e.g. validate deadline is in future)
        # For now, just create the entity
        task = Task(
            id=None, # DB will assign ID
            title=title,
            user_id=user_id,
            description=description,
            deadline=deadline
        )
        return await self.repository.create(task)
