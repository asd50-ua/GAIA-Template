# User Stories: Task Management (Gestión de Tareas)

**Feature:** Task Management (`task-management`)  
**Role:** Student  
**Objectives:** Increase task completion, reduce anxiety through organization.

---

## Story List

| ID | Title | Priority |
|---|---|---|
| **TM-STUDENT-001** | Create a new task | High |
| **TM-STUDENT-002** | View list of tasks | High |
| **TM-STUDENT-003** | Update task details | Medium |
| **TM-STUDENT-004** | Mark task as completed/pending | High |
| **TM-STUDENT-005** | Delete a task | Low |
| **TM-STUDENT-006** | Filter and sort tasks | Medium |

---

## Detailed Stories

### TM-STUDENT-001: Create a new task
**As a** Student  
**I want to** create a new task with a title, description, and deadline  
**So that** I can record what I need to do for my TFG.

PO Notes:
- Title is mandatory.
- Default status is "Pending".
- Deadline is optional but recommended.

**Acceptance Criteria (BDD):**

```gherkin
Scenario: Successfully creating a task
  Given I am logged in as a Student
  When I choose to create a new task
  And I enter the title "Draft Introduction"
  And I select a deadline "2026-03-15"
  And I submit the task
  Then the system saves the task
  And I see "Draft Introduction" in my task list
  And the operation completes in under 100ms

Scenario: Attempting to create a task without title
  Given I am logged in as a Student
  When I try to create a task with an empty title
  Then I should see a validation error "Title is required"
  And the task is not saved
```

---

### TM-STUDENT-002: View list of tasks
**As a** Student  
**I want to** see a list of my own tasks  
**So that** I know what remains to be done.

PO Notes:
- Must only show tasks belonging to the logged-in user (Security).
- Should display visual indicators for status and deadline proximity.

**Acceptance Criteria (BDD):**

```gherkin
Scenario: Viewing my own tasks
  Given I have 3 existing tasks
  When I view the task list
  Then I should see exactly those 3 tasks
  And the list should load in under 200ms

Scenario: Security - Isolation of data
  Given User "Alice" has tasks
  And I am logged in as "Bob"
  When I view the task list
  Then I should NOT see any of "Alice's" tasks
```

---

### TM-STUDENT-003: Update task details
**As a** Student  
**I want to** edit the title, description, or deadline of a task  
**So that** I can correct mistakes or update plans.

**Acceptance Criteria (BDD):**

```gherkin
Scenario: Update a task description
  Given I have a task "Draft Intro"
  When I update the description to "Draft Intro v2"
  Then the changes are saved
  And I see the updated description when viewing the task

Scenario: Update non-existent task
  Given I try to update a task with ID "9999"
  Then I should receive a "Not Found" error
```

---

### TM-STUDENT-004: Mark task as completed/pending
**As a** Student  
**I want to** toggle the status of a task  
**So that** I can track my progress visually.

PO Notes:
- This is a high-frequency action.
- Visual feedback (strikethrough) is crucial.

**Acceptance Criteria (BDD):**

```gherkin
Scenario: Mark task as done
  Given I have a task "Read Papers" with status "Pending"
  When I mark the task as "Completed"
  Then the status changes to "Completed"
  And the task appears crossed out or visually distinct

Scenario: Reopen a task
  Given I have a task "Read Papers" with status "Completed"
  When I mark the task as "Pending"
  Then the status changes to "Pending"
```

---

### TM-STUDENT-005: Delete a task
**As a** Student  
**I want to** delete a task permanently  
**So that** I can remove duplicate or mistakenly created items.

**Acceptance Criteria (BDD):**

```gherkin
Scenario: Delete an existing task
  Given I have a task "Mistake"
  When I delete the task "Mistake"
  Then the task is removed from my list
  And I cannot retrieve it anymore

Scenario: Try to delete another user's task
  Given I know the ID of "Alice's" task
  When I try to delete that task
  Then I should be denied permission (403 or 404)
```

---

### TM-STUDENT-006: Filter and Sort tasks
**As a** Student  
**I want to** filter my list by status or sort by deadline  
**So that** I can focus on immediate priorities.

PO Notes:
- Filters: All, Pending, Completed.
- Sort: Deadline (ascending), Created (descending).

**Acceptance Criteria (BDD):**

```gherkin
Scenario: Filter by Pending
  Given I have 2 Pending tasks and 1 Completed task
  When I apply the filter "Pending"
  Then I should see only the 2 Pending tasks

Scenario: Sort by Deadline
  Given I have task A (deadline tomorrow) and task B (deadline today)
  When I sort by "Deadline Ascending"
  Then I should see task B before task A
```
