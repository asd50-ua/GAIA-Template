from app.domain.entities.task import Task
from app.infrastructure.models.task import TaskModel

class TaskMapper:
    @staticmethod
    def to_domain(model: TaskModel) -> Task:
        return Task(
            id=model.id,
            title=model.title,
            description=model.description,
            deadline=model.deadline,
            status=model.status,
            user_id=model.user_id,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    @staticmethod
    def to_model(entity: Task) -> TaskModel:
        return TaskModel(
            id=entity.id if entity.id else None,
            title=entity.title,
            description=entity.description,
            deadline=entity.deadline,
            status=entity.status,
            user_id=entity.user_id
        )
