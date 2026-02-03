# TM-STUDENT-001-FE-T01 — Implementation Plan

**Source ticket**: `specs/features/task-management/tickets.md` → **TM-STUDENT-001-FE-T01**  
**Related user story**: **TM-STUDENT-001** (from `specs/features/task-management/user-stories.md`)  
**Plan version**: v1.0 — (Agent, 2026-02-03)  
**Traceability**: All tasks must include inline references to `TM-STUDENT-001-FE-T01`.

---

## 1) Context & Objective
- **Ticket summary**: Implement the frontend "Create Task" form. This allows students to input a title, description, and optional deadline, and submit it to the backend.
- **Impacted entities/tables**: N/A (Frontend only).
- **Impacted services/modules**: Frontend Scaffolding, `features/tasks/components/CreateTaskForm`, `api/tasks`, Routing.
- **Impacted tests or business flows**: `Successfully creating a task`, `Attempting to create a task without title`.

## 2) Scope
- **In scope**:
  - Scaffolding the `frontend` application (React + Vite + TS + Tailwind + Shadcn).
  - Configuring Brand Identity (Colors, Typography) in Tailwind.
  - Setting up API Client (Axios) and Query Client (TanStack Query).
  - Implementing `CreateTaskPage` and `CreateTaskForm` components.
  - Form validation using Zod.
  - Integration with `POST /api/v1/tasks`.
- **Out of scope**:
  - Implementation of other Task Management stories (List, Edit, Delete).
  - Authentication (Will use a hardcoded token or simple context for now until Auth feature is ready).
- **Assumptions**: 
  - Backend is running on `http://localhost:8000` (mapped to `8005` on host).
  - We use `shadcn/ui` components for consistency.
- **Open questions**: None.

## 3) Detailed Work Plan (TDD + BDD)
> **Container Check**: ensure `docker-compose.yml` is running.
> **Note**: Since `frontend/` does not exist, Task 1 is explicitly about bootstrapping.

### 3.1 Test-first sequencing
1.  **Scaffold**: Initialize Vite app & Testing setup.
2.  **Unit Tests**: Create tests for `CreateTaskForm` (rendering, validation logic).
3.  **Implementation**: Build components to pass tests.
4.  **Integration**: Verify API call via MSW (Mock Service Worker) or manual integration.

### 3.2 NFR hooks
- **Brand**: Use `--color-action-primary` (Terracotta AA) for the submit button. Use Inter font.
- **Accessibility**: Form labels must be visible. Inputs must have accessible names.
- **Validation**: Title is mandatory. Date must be valid.
- **Feedback**: Show loading state (spinner/disabled button) during submission.

## 4) Atomic Task Breakdown

### Task 1: Scaffold Frontend & Brand Config
- **Purpose**: Initialize the frontend codebase with the required stack (`TM-STUDENT-001-FE-T01`).
- **Prerequisites**: Node.js installed.
- **Artifacts impacted**: `frontend/`, `package.json`, `tailwind.config.js`, `src/styles/globals.css`.
- **Test types**: Manual (Build success).
- **BDD Acceptance**:
  - Given I have no frontend
  - When I run the scaffold commands
  - Then I have a running Vite+React app with Tailwind configured with Brand colors.

### Task 2: Setup Core Architecture (API, Routing, Query)
- **Purpose**: Establish the foundation for features (`TM-STUDENT-001-FE-T01`).
- **Prerequisites**: Task 1.
- **Artifacts impacted**: `frontend/src/app/providers/`, `frontend/src/api/http.ts`, `frontend/src/app/router/`.
- **Test types**: Unit (Client configuration).
- **BDD Acceptance**:
  - Given the app is initialized
  - When I check the Axios instance
  - Then it points to `VITE_API_BASE_URL`.

### Task 3: Setup Testing Infrastructure
- **Purpose**: Enable TDD for UI components (`TM-STUDENT-001-FE-T01`).
- **Prerequisites**: Task 1.
- **Artifacts impacted**: `vitest.config.ts`, `src/test/setup.ts`, `src/test/utils.tsx`.
- **Test types**: Manual (Test run).
- **BDD Acceptance**:
  - Given I run `npm run test`
  - Then it executes successfully.

### Task 4: Implement Create Task Form (TDD)
- **Purpose**: The actual UI for creating tasks (`TM-STUDENT-001-FE-T01`).
- **Prerequisites**: Task 3.
- **Artifacts impacted**: `features/tasks/components/CreateTaskForm.tsx`, `features/tasks/api/createTask.ts`, `features/tasks/pages/CreateTaskPage.tsx`.
- **Test types**: Component Test (`CreateTaskForm.test.tsx`).
- **BDD Acceptance**:
  - Given I am on the Create Task page
  - When I submit empty form
  - Then I see "Title is required".
  - When I submit valid data
  - Then `createTask` mutation is called.

### Task 5: Verify & Register
- **Purpose**: Ensure compliance and document.
- **Prerequisites**: Task 4.
- **Artifacts impacted**: `specs/features/task-management/tickets.md`.
- **Test types**: Manual/Regression.
