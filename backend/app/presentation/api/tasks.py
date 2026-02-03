# [Feature: Task Management] [Story: TM-STUDENT-001] [Ticket: TM-STUDENT-001-BE-T01]
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db
from app.core.security import get_current_user, User
from app.presentation.schemas.task import CreateTaskRequest, TaskResponse
from app.infrastructure.repositories.task_repository_impl import TaskRepositoryImpl
from app.application.use_cases.tasks.create_task import CreateTaskUseCase

router = APIRouter()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    request: CreateTaskRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    repository = TaskRepositoryImpl(db)
    use_case = CreateTaskUseCase(repository)
    
    return await use_case.execute(
        title=request.title,
        user_id=current_user.id,
        description=request.description,
        deadline=request.deadline
    )
