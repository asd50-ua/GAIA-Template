from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.task import Task
from app.domain.repositories.task_repository import TaskRepository
from app.infrastructure.models.task import TaskModel
from app.infrastructure.db.mappers.task_mapper import TaskMapper

class TaskRepositoryImpl(TaskRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, task: Task) -> Task:
        model = TaskMapper.to_model(task)
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return TaskMapper.to_domain(model)
