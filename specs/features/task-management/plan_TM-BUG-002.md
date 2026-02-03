# TM-BUG-002 — Fix Tailwind CSS PostCSS Configuration

**Ticket**: `TM-BUG-002`
**Source**: User Report (Vite Build Error)

## 1. Issue Description
Running the frontend fails with:
`[postcss] It looks like you're trying to use 'tailwindcss' directly as a PostCSS plugin. The PostCSS plugin has moved to a separate package... install @tailwindcss/postcss`.

## 2. Root Cause
Tailwind CSS v4 was installed (`^4.0.0`), which requires a dedicated PostCSS plugin `@tailwindcss/postcss` instead of the main `tailwindcss` package in `postcss.config.js`.

## 3. Proposed Fix
1. Install `@tailwindcss/postcss` as a dev dependency.
2. Update `postcss.config.js` to use `@tailwindcss/postcss`.

## 4. Verification Plan
1. Rebuild frontend: `docker compose build frontend`.
2. Start frontend: `docker compose up frontend`.
3. Verify no build errors.

## 5. Tasks
- [ ] Install `@tailwindcss/postcss` in `frontend/package.json`.
- [ ] Update `frontend/postcss.config.js`.
- [ ] Mark ticket as COMPLETED.
