from uuid import UUID
from datetime import datetime, date
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"

class Task:
    def __init__(
        self,
        id: int,
        title: str,
        user_id: int,
        description: Optional[str] = None,
        deadline: Optional[date] = None,
        status: TaskStatus = TaskStatus.PENDING,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.title = title
        self.user_id = user_id
        self.description = description
        self.deadline = deadline
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
