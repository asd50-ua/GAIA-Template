from pydantic import BaseModel, ConfigDict, Field
from datetime import date, datetime
from typing import Optional
from app.domain.entities.task import TaskStatus

class CreateTaskRequest(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the task")
    description: Optional[str] = Field(None, description="Detailed description")
    deadline: Optional[date] = Field(None, description="Due date")

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    deadline: Optional[date]
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
