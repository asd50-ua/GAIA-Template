# TM-STUDENT-001-BE-T01 — Implementation Plan

**Source ticket**: `specs/features/task-management/tickets.md` → **TM-STUDENT-001-BE-T01**  
**Related user story**: **TM-STUDENT-001** (from `specs/features/task-management/user-stories.md`)  
**Plan version**: v1.0 — (Agent, 2026-02-03)  
**Traceability**: All tasks must include inline references to `TM-STUDENT-001-BE-T01`.

---

## 1) Context & Objective
- **Ticket summary**: Implement the backend logic to create a new task. This includes the API endpoint `POST /api/v1/tasks`, domain entity, repository, and service logic.
- **Impacted entities/tables**: `tasks`.
- **Impacted services/modules**: New `tasks` domain (Application, Domain, Infrastructure, Presentation). Auth dependency.
- **Impacted tests or business flows**: `Successfully creating a task`, `Attempting to create a task without title`.

## 2) Scope
- **In scope**:
  - Scaffolding the `tasks` domain using `fastapi-domain-generator`.
  - Scaffolding the test infrastructure using `setup-backend-testing`.
  - Stubbing Auth dependency (`get_current_user`) to enable development.
  - Implement `CreateTaskUseCase`.
  - Implement `TaskRepository` (SQLAlchemy).
  - Implement `POST /tasks` endpoint with Pydantic validation.
- **Out of scope**:
  - Full Auth implementation (login/signup endpoints).
  - Frontend integration.
- **Assumptions**: 
  - We will use a dummy user (ID 1) or a basic mock for auth until the Auth module is fully ready.
- **Open questions**: None.

## 3) Detailed Work Plan (TDD + BDD)
> **Container Check**: Ensure `docker-compose.yml` is running (`docker compose up -d`).

### 3.1 Test-first sequencing
1.  **Scaffold Testing**: Initialize `backend/tests` structure if missing.
2.  **Scaffold Domain**: Create file structure for `tasks` domain.
3.  **Define Domain Entity**: `Task` dataclass.
4.  **Unit Tests (Service)**: Test `CreateTaskUseCase` with mocked repository.
5.  **Integration Tests (Repository)**: Verify `save` method with actual DB.
6.  **Contract/E2E Tests (API)**: Verify endpoint returns 201 and validated JSON.

### 3.2 NFR hooks
- **Security**: Endpoint MUST depend on `get_current_user`.
- **Performance**: Repository should use async DB driver.
- **Validation**: Pydantic schemas for `CreateTaskRequest`.

## 4) Atomic Task Breakdown

### Task 1: Scaffold Backend Testing & Domains
- **Purpose**: Prepare the codebase structure for the new feature (`TM-STUDENT-001-BE-T01`).
- **Prerequisites**: Docker running.
- **Artifacts impacted**: `backend/tests/`, `backend/app/[domain, application, infrastructure, presentation]`.
- **Test types**: Check file existence.
- **BDD Acceptance**:
  - Given the backend folder
  - When I check for `backend/tests` and `backend/app/domain/entities/task.py`
  - Then they should exist (after running generation).

### Task 2: Implement Auth Stub
- **Purpose**: Provide a `get_current_user` dependency to enforce ownership in `TM-STUDENT-001-BE-T01`.
- **Prerequisites**: Task 1.
- **Artifacts impacted**: `backend/app/core/security.py` (or `dependencies.py`).
- **Test types**: Unit.
- **BDD Acceptance**:
  - When I call `get_current_user` with a valid token (or mock)
  - Then it returns a user object with `id`.

### Task 3: Domain & Repository Implementation (TDD)
- **Purpose**: Core business logic and persistence for Tasks.
- **Prerequisites**: Task 2.
- **Artifacts impacted**: `Task` entity, `TaskRepository` (interface + impl), `TaskModel` (SQLAlchemy).
- **Test types**: Unit (Mapper), Integration (Repository).
- **BDD Acceptance**:
  - Given a valid Task entity
  - When I call `repository.save(task)`
  - Then it is persisted to PostgreSQL.

### Task 4: Use Case & API Endpoint (TDD)
- **Purpose**: Expose the functionality via HTTP (`TM-STUDENT-001-BE-T01`).
- **Prerequisites**: Task 3.
- **Artifacts impacted**: `CreateTaskUseCase`, `routers/tasks.py`, `schemas/task.py`.
- **Test types**: API Test (`httpx`).
- **BDD Acceptance**:
  - Given I am authenticated
  - When I POST to `/api/v1/tasks` with valid data
  - Then I receive 201 Created and the created task payload.
  - When I POST with missing title
  - Then I receive 422 Unprocessable Entity.

### Task 5: Verify & Register
- **Purpose**: Ensure architecture compliance and update docs.
- **Prerequisites**: Task 4.
- **Artifacts impacted**: `backend/app/main.py` (include router), `specs/ArchitecturalModel.md`.
- **Test types**: Manual/Regression.
