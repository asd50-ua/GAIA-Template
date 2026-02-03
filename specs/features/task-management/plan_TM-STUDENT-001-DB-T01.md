# TM-STUDENT-001-DB-T01 — Implementation Plan

**Source ticket**: `specs/features/task-management/tickets.md` → **TM-STUDENT-001-DB-T01**  
**Related user story**: **TM-STUDENT-001** (from `specs/features/task-management/user-stories.md`)  
**Plan version**: v1.0 — (Agent, 2026-02-03)  
**Traceability**: All tasks must include inline references to `TM-STUDENT-001-DB-T01` and `Successfully creating a task`.

---

## 1) Context & Objective
- **Ticket summary**: Initialize the database schema for Task Management. This involves creating the `tasks` table to store title, description, deadline, status, and user ownership.
- **Impacted entities/tables**: `tasks`, `users` (new/dependency).
- **Impacted services/modules**: Backend scaffolding, Database Schema (Alembic).
- **Impacted tests or business flows**: Foundation for `Successfully creating a task`.

## 2) Scope
- **In scope**:
  - Bootstrapping the Backend project structure (FastAPI + Alembic).
  - Configuring `docker-compose` for PostgreSQL.
  - Creating `users` table (hard dependency).
  - Creating `tasks` table with foreign key to `users`.
  - Verifying migrations apply and rollback cleanly.
- **Out of scope**:
  - Implementation of API endpoints (handled in BE ticket).
  - User management logic (only schema is in scope).
- **Assumptions**: 
  - Project is greenfield; proceeding with full initialization.
  - Using `postgresql` as the database.
- **Open questions**: None.

## 3) Detailed Work Plan (TDD + BDD)
> **Container Check**: Ensure a distinct `docker-compose.yml` exists. If missing, generate it immediately.

### 3.1 Test-first sequencing
1.  **Define Architecture**: Establish `backend/` strict structure as per `@/.agent/rules/techstack-backend.md`.
2.  **Infrastructure Tests**: Create a "schema test" that spins up the DB container, applies migrations, and inspects the information schema to verify table existence.
3.  **Minimal Implementation**: Write the Alembic migrations.
4.  **Refactor**: Ensure naming conventions match `DataModel.md`.

### 3.2 NFR hooks
- **Security/Privacy**: `users` table should be prepared for secure password storage (if needed later) or just basic identity. `tasks` table is RLS-ready via `user_id`.
- **Resilience**: Migrations must be transactional.
- **Documentation**: Create `@/specs/DataModel.md` to reflect the new schema.

## 4) Atomic Task Breakdown

### Task 1: Scafold Backend & Docker Environment
- **Purpose**: Establish the runtime environment required to run migrations (`TM-STUDENT-001-DB-T01`).
- **Prerequisites**: None.
- **Artifacts impacted**: `docker-compose.yml`, `backend/pyproject.toml`, `backend/alembic/`, `backend/app/core/config.py`.
- **Test types**: Integration (Docker up).
- **BDD Acceptance**:
  - Given the project is empty
  - When I run `docker compose up -d`
  - Then a PostgreSQL container is healthy on port 5432.

### Task 2: Setup Alembic & Users Table (Dependency)
- **Purpose**: Create the necessary user relation for the tasks table (`TM-STUDENT-001-DB-T01`).
- **Prerequisites**: Task 1 complete.
- **Artifacts impacted**: `backend/alembic/env.py`, `backend/alembic/versions/xxxx_create_users.py`.
- **Test types**: Unit (Migration applied).
- **BDD Acceptance**:
  - Given I have a healthy DB
  - When I run `alembic upgrade head`
  - Then the `users` table exists.

### Task 3: Create Tasks Table Migration
- **Purpose**: Implement the core requirement (`TM-STUDENT-001-DB-T01`).
- **Prerequisites**: Task 2 complete.
- **Artifacts impacted**: `backend/alembic/versions/xxxx_create_tasks.py`.
- **Test types**: Unit (Migration applied).
- **BDD Acceptance**:
  - Given I have the `users` table
  - When I run the tasks migration
  - Then the `tasks` table exists with columns `id`, `title`, `description`, `deadline`, `status`, `user_id`.
  - And `user_id` is a foreign key to `users`.

### Task 4: Verify & Document
- **Purpose**: Ensure drift-free documentation (`TM-STUDENT-001-DB-T01`).
- **Prerequisites**: Task 3 complete.
- **Artifacts impacted**: `@/specs/DataModel.md`.
- **Test types**: Manual Review.
- **BDD Acceptance**:
  - Given the schema is applied
  - When I check the documentation
  - Then `DataModel.md` accurately describes the `users` and `tasks` entities.
