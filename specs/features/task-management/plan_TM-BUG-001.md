# TM-BUG-001 — Fix Vite Node Version Incompatibility

**Ticket**: `TM-BUG-001`
**Source**: User Report (Docker error)

## 1. Issue Description
When running `docker compose up`, the frontend container fails with `TypeError: crypto.hash is not a function` and a message stating that Vite requires Node.js 20.19+ or 22.12+.
The current `frontend/Dockerfile` uses `node:18-alpine`.

## 2. Root Cause
Vite 6/7 has dropped support for Node 18, which is what `node:18-alpine` provides.

## 3. Proposed Fix
Upgrade the base image in `frontend/Dockerfile` to `node:22-alpine` (LTS is 22).

## 4. Verification Plan
1. Rebuild the frontend container: `docker compose build frontend`.
2. Start the container: `docker compose up frontend`.
3. Verify logs show Vite server started successfully.

## 5. Tasks
- [ ] Upgrade `frontend/Dockerfile` to `node:22-alpine`.
- [ ] Verify build and startup.
- [ ] Update `tickets.md` to COMPLETED.
