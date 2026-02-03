# [Feature: Task Management] [Story: TM-STUDENT-001] [Ticket: TM-STUDENT-001-BE-T01]
from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.task import Task

class TaskRepository(ABC):
    @abstractmethod
    async def create(self, task: Task) -> Task:
        pass
