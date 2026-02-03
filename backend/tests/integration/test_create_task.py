import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio(loop_scope="session")

async def test_create_task_happy_path(client: AsyncClient):
    # Given I am an authenticated user (mocked in security.py stub)
    payload = {
        "title": "Finish TFG",
        "description": "Write the memory",
        "deadline": "2026-06-01"
    }
    
    # When I create a task
    response = await client.post("/api/v1/tasks/", json=payload, headers={"Authorization": "Bearer dummy"})
    
    # Then I receive 201 Created
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["id"] is not None
    assert data["status"] == "PENDING"

async def test_create_task_missing_title(client: AsyncClient):
    # Given a payload without title
    payload = {
        "description": "No title provided"
    }
    
    # When I create a task
    response = await client.post("/api/v1/tasks/", json=payload, headers={"Authorization": "Bearer dummy"})
    
    # Then I receive 422 Validation Error
    assert response.status_code == 422
