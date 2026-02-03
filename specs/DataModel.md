# Data Model

## ER Diagram

```mermaid
erDiagram
    USERS {
        int id PK
        string email
        string full_name
        string hashed_password
        boolean is_active
        datetime created_at
    }
    TASKS {
        int id PK
        string title
        text description
        date deadline
        enum status "PENDING, COMPLETED"
        int user_id FK
        datetime created_at
        datetime updated_at
    }
    USERS ||--o{ TASKS : "has many"
```

## Schema Definitions

### Users
- **id**: Primary Key
- **email**: Unique, Indexed
- **full_name**: Optional
- **hashed_password**: Security sensitive
- **is_active**: Boolean flag
- **created_at**: Timestamp

### Tasks
- **id**: Primary Key
- **title**: Mandatory
- **description**: Optional text
- **deadline**: Optional date
- **status**: Enum (PENDING, COMPLETED), default PENDING
- **user_id**: Foreign Key to Users.id
- **timestamps**: created_at, updated_at
