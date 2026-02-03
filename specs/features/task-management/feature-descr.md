# Feature Spec: Task Management (Gestión de Tareas)

## 0) Feature Name & Summary
**Feature Name:** Task Management (Gestión de Tareas)

**Executive Summary (3–5 lines):**  
- **Problem:** Students struggle with disorganization, using multiple disconnected tools (Excel, Notion, paper) to track TFG progress.  
- **Opportunity:** Centralizing task management reduces cognitive load and anxiety, allowing students to focus on research and writing.  
- **Expected Outcome:** Higher task completion rates and fewer missed deadlines due to clear visibility of "what to do next".  

**Fit with Vision / Product Goal:**  
This is the core operational engine of the "Guide" value proposition, enabling the student to break down the massive TFG project into manageable steps.

---

## 1) Description of the feature 
The Task Management feature allows students to create, tracking, and organize the specific activities required to complete their TFG. Unlike generic to-do lists, this feature is the central hub where the student translates the theoretical sections of their thesis into actionable work items.

It supports the complete lifecycle of a task: creation, execution (state tracking), and completion. It provides immediate visual feedback on progress and helps prioritize work based on deadlines.

---

## 2) Users/Roles & Impacted Personas
`[Who uses or is affected by the feature]`

| Role/Persona | Key Objectives | Tasks / Jobs-to-be-done | Current Pain | Stakeholders |
|---|---|---|---|---|
| **Student (Alumno)** | Organize TFG workload, meet deadlines | Create tasks, mark as done, check deadlines | Overwhelmed by project size, "analysis paralysis" | Tutor (indirectly benefits from progress) |
| **System Admin** | Ensure system stability | Monitor usage metrics | N/A | |

---

## 3) Problem / Opportunity Statement
**Context:** The TFG is often the first large-scale, self-directed project a student faces.  
**Problem Statement:** Our **Students** experience **anxiety and disorganization** when **trying to plan their work**, which causes **procrastination and missed deadlines**.  
**Why Now:** As the core component of the MVP, this feature is a prerequisite for any progress tracking or dashboard functionality.

---

## 4) Objectives & Business Outcomes

| Objective / Outcome | KPI / Metric | Baseline | Target | Time Horizon | Measurement Method |
|---|---|---|---|---|---|
| Increase user engagement | Tasks created per user | 0 | > 20/TFG | MVP Period | DB Analysis |
| Improve completion rate | % of tasks marked 'Done' | N/A | > 70% | MVP Period | DB Analysis |
| Reduce dropout risk | Days since last activity | N/A | < 7 days | MVP Period | Analytics Event |

---

## 5) Scope (In/Out)

**In scope:**  
- **CRUD Operations:** Create, Read, Update, Delete tasks.  
- **Attributes:** Title, Description, Deadline, Status (Pending, In Progress, Completed).  
- **Filtering/Sorting:** By status and deadline.  
- **Visual Feedback:** Strikethrough or visual cue for completed tasks.  

**Out of scope (to prevent scope creep):**  
- **Subtasks / Checklist inside tasks** (stick to atomic tasks for MVP).  
- **Recurring tasks.**  
- **Calendar View** (List view only for MVP).  
- **Tutor assignment** (Tutor view is future scope).  
- **Drag-and-drop ordering** (Simple sort by date/status first).

**Key Assumptions:**  
- Students are the sole owners of their tasks (no team TFGs for MVP).  
- Mobile usage is critical (must be responsive).

**Dependencies / Blockers:**  
- Auth system (users must be logged in to own tasks).

---

## 6) Non-Functional Requirements (NFRs)

### 6.1 Security & Privacy
- **Access Control:** A user can ONLY access tasks linked to their `user_id`. Strict Row-Level Security (RLS) or application-level filtering.  
- **Data Protection:** Task descriptions are encrypted in transit (TLS).

### 6.2 Performance
- **Latency:** Task creation and status toggle must feel instant (< 100ms).  
- **List Loading:** Main task list loads in < 200ms (P95).

### 6.3 Availability & Reliability
- **Offline-ish:** No data loss if network flickers; usage of cheerful optimistic UI updates recommended.

### 6.4 Accessibility (a11y) & Internationalization (i18n)
- **A11y:** Status changes must be announced to screen readers (ARIA). Keyboard navigable.  
- **Language:** UI labels in Spanish (Castilian).

### 6.5 Observability
- **Metrics:** Track `task_created`, `task_completed` events.  
- **Logs:** Error logs for failed CRUD operations.

---

### Annexes (optional)
- **Risks:** Students might stop using it if manual entry is too tedious. -> Mitigation: Make creation extremely fast (one-line input).
