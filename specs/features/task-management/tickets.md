# Task Management — Implementation Tickets

**Feature:** Task Management (`task-management`)
**Dependencies:** Authentication module (User ID required).

---

### Story: TM-STUDENT-001 — Create a new task
**Source**: `user-stories.md`
**Key Scenarios**: `Successfully creating a task`, `Attempting to create a task without title`

#### Tickets for TM-STUDENT-001

1. - [x] **TM-STUDENT-001-DB-T01 — Create Tasks Table** (2026-02-03)
   - **Type**: DB
   - **Description**: create `tasks` table with fields: `id` (PK), `title` (not null), `description` (text), `deadline` (date, nullable), `status` (enum: PENDING, COMPLETED, default=PENDING), `user_id` (FK to users).
   - **Scope**: Migration script + Rollback.
   - **Dependencies**: Users table.

2. - [x] **TM-STUDENT-001-BE-T01 — Create Task Endpoint** (2026-02-03)
   - **Type**: BE
   - **Description**: Implement `POST /api/v1/tasks`. Validates input (Pydantic). Enforces `user_id` from auth context. Returns 201 Created.
   - **Scope**: Controller, Service, Repository, DTOs, Unit Tests.

3. - [x] **TM-STUDENT-001-FE-T01 — Task Creation Form** (2026-02-03)
   - **Type**: FE
   - **Description**: UI component to input title, description, deadline. Uses Zod for validation (Title required).
   - **Scope**: Component, API Client integration, React Query mutation.

---

### Story: TM-STUDENT-002 — View list of tasks
**Source**: `user-stories.md`
**Key Scenarios**: `Viewing my own tasks`, `Security - Isolation of data`

#### Tickets for TM-STUDENT-002

1. - [ ] **TM-STUDENT-002-DB-T01 — Index Tasks by User**
   - **Type**: DB
   - **Description**: Ensure index on `user_id` for efficient retrieval.
   - **Scope**: Migration (if not created implicitly), verification.

2. - [ ] **TM-STUDENT-002-BE-T01 — List Tasks Endpoint**
   - **Type**: BE
   - **Description**: Implement `GET /api/v1/tasks`. Returns list of tasks for current user.
   - **Scope**: Repository `findAllByUser`, Controller, Tests. Explicit anti-BOLA check (use auth context, do NOT accept user_id param).

3. - [ ] **TM-STUDENT-002-FE-T01 — Task List Component**
   - **Type**: FE
   - **Description**: Display tasks in a list. Show status visual indicator.
   - **Scope**: `TaskList` component, fetching with React Query (loading/error states).

---

### Story: TM-STUDENT-003 — Update task details
**Source**: `user-stories.md`
**Key Scenarios**: `Update a task description`, `Update non-existent task`

#### Tickets for TM-STUDENT-003

1. - [ ] **TM-STUDENT-003-BE-T01 — Update Task Endpoint**
   - **Type**: BE
   - **Description**: Implement `PATCH /api/v1/tasks/{id}`. Only owner can update.
   - **Scope**: Validation (404 if not found, 403 if not owner). DTO `UpdateTaskRequest`.

2. - [ ] **TM-STUDENT-003-FE-T01 — Task Edit UI**
   - **Type**: FE
   - **Description**: Edit mode or Modal to update task details.
   - **Scope**: Prefill form data, Mutation `updateTask`.

---

### Story: TM-STUDENT-004 — Mark task as completed/pending
**Source**: `user-stories.md`
**Key Scenarios**: `Mark task as done`, `Reopen a task`

#### Tickets for TM-STUDENT-004

1. - [ ] **TM-STUDENT-004-BE-T01 — Toggle Status Endpoint**
   - **Type**: BE
   - **Description**: Reuse `PATCH` or create `PATCH /tasks/{id}/status`. Logic to toggle status.
   - **Scope**: Service logic, Tests.

2. - [ ] **TM-STUDENT-004-FE-T01 — Status Checkbox**
   - **Type**: FE
   - **Description**: Checkbox usage in list item.
   - **Scope**: Optimistic Update (UI toggles immediately).

---

### Story: TM-STUDENT-005 — Delete a task
**Source**: `user-stories.md`
**Key Scenarios**: `Delete an existing task`, `Try to delete another user's task`

#### Tickets for TM-STUDENT-005

1. - [ ] **TM-STUDENT-005-BE-T01 — Delete Task Endpoint**
   - **Type**: BE
   - **Description**: Implement `DELETE /api/v1/tasks/{id}`.
   - **Scope**: Owner verification (critical). Hard delete.

2. - [ ] **TM-STUDENT-005-FE-T01 — Delete Action**
   - **Type**: FE
   - **Description**: Delete button with confirmation dialog.
   - **Scope**: Cache invalidation (remove from list).

---

### Story: TM-STUDENT-006 — Filter and Sort tasks
**Source**: `user-stories.md`
**Key Scenarios**: `Filter by Pending`, `Sort by Deadline`

#### Tickets for TM-STUDENT-006

1. - [ ] **TM-STUDENT-006-DB-T01 — Indexes for Filtering**
   - **Type**: DB
   - **Description**: Add index on `status` and `deadline` (composite with user_id likely beneficial).
   - **Scope**: Migration.

2. - [ ] **TM-STUDENT-006-BE-T01 — Filter/Sort Logic**
   - **Type**: BE
   - **Description**: Enhance `GET /tasks` with query params `status` (enum) and `sort_by` (date).
   - **Scope**: Repository query builder modifications.

3. - [ ] **TM-STUDENT-006-FE-T01 — Filter Controls**
   - **Type**: FE
   - **Description**: UI controls (Dropdown/Tabs) to switch views.
   - **Scope**: State management for filters, re-fetching tasks with params.

### Bug Fixes

1. - [x] **TM-BUG-001 — Fix Vite Node Version Incompatibility** (2026-02-03)
   - **Type**: DEV
   - **Description**: Upgrade `frontend/Dockerfile` base image to Node 20+, as Vite requires it. Fixes `crypto.hash is not a function`.
   - **Scope**: `frontend/Dockerfile`.

2. - [ ] **TM-BUG-002 — Fix Tailwind CSS PostCSS Configuration**
   - **Type**: DEV
   - **Description**: Install `@tailwindcss/postcss` and update `postcss.config.js` to support Tailwind v4.
   - **Scope**: `frontend/package.json`, `frontend/postcss.config.js`.
