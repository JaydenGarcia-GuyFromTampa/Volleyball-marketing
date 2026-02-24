# Volleyball Marketing App

Full-stack volleyball marketing application: **Django** (backend, auth, REST API, PostgreSQL) + **Vue 3** (frontend), run with **Docker** and **Poetry**.

## Architecture (summary)

| Component   | Stack        | Role |
|------------|---------------|------|
| Frontend   | Vue 3, Vite, Pinia, Vue Router | SPA; login, register, dashboard, campaigns; JWT in localStorage, axios interceptors for refresh |
| Backend    | Django 5, DRF, Simple JWT, CORS, Gunicorn | REST API, auth (register/login/refresh/me), campaigns & events CRUD, external API stub |
| Database   | PostgreSQL 15 | Persisted data |
| Runtime    | Docker Compose | `db`, `backend`, `frontend` (nginx serving built Vue + proxy `/api` to backend) |

**Auth:** JWT access + refresh; access in `Authorization: Bearer`; refresh used when access expires (401). Register returns tokens so user is logged in after signup.

**APIs:** Backend exposes `/api/auth/*` and `/api/campaigns/`, `/api/events/`, `/api/external/`. Optional `EXTERNAL_API_BASE_URL` for external integrations (see `campaigns.services.call_external_api`).

## Prerequisites

- Docker and Docker Compose
- For local backend/frontend dev: Python 3.11+, Node 20+, Poetry (backend), npm (frontend)

## Run with Docker (recommended)

1. Clone and go to project root:
   ```bash
   cd volleyball-marketing
   ```

2. Create env (optional; defaults work for dev):
   ```bash
   cp .env.example .env
   ```

3. Build and start:
   ```bash
   docker compose up --build
   ```

4. Open:
   - **App:** http://localhost (frontend; nginx proxies `/api` to backend)
   - **API only:** http://localhost:8000 (backend)
   - **Admin:** http://localhost:8000/admin/ (create a superuser first)

5. Create Django superuser (one-off):
   ```bash
   docker compose exec backend python manage.py createsuperuser
   ```

## Local development (without Docker)

### Backend (Poetry + Django)

```bash
cd volleyball-marketing
poetry install
cd backend
# Use a local PostgreSQL or run only DB in Docker: docker compose up -d db
export POSTGRES_HOST=localhost
export POSTGRES_PASSWORD=postgres
# ... other POSTGRES_* as needed
poetry run python manage.py migrate
poetry run python manage.py runserver
```

### Frontend (Vite)

```bash
cd volleyball-marketing/frontend
npm install
npm run dev
```

Frontend runs at http://localhost:5173 and proxies `/api` to the backend (configure in `vite.config.js`).

## Project layout

```
volleyball-marketing/
├── pyproject.toml          # Poetry deps (backend)
├── docker-compose.yml
├── .env.example
├── backend/
│   ├── Dockerfile
│   ├── entrypoint.sh       # wait for DB, migrate, then gunicorn
│   ├── manage.py
│   ├── backend/            # Django config (settings, urls, wsgi)
│   ├── accounts/            # User model, auth API (login, register, me, refresh)
│   ├── campaigns/          # Campaign & Event models, CRUD API, external API stub
│   └── ...
└── frontend/
    ├── Dockerfile          # build Vue, nginx serve + /api proxy
    ├── nginx.conf
    ├── package.json
    ├── src/
    │   ├── api/            # axios + JWT interceptors
    │   ├── router/         # Vue Router, auth guards
    │   ├── stores/         # Pinia auth store
    │   └── views/         # Login, Register, Dashboard, Campaigns
    └── ...
```

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| JWT in localStorage (XSS) | Prefer short-lived access token; refresh in memory or httpOnly cookie if you need higher security. |
| DB not ready at startup | Entrypoint waits for PostgreSQL and runs migrations before starting Gunicorn. |
| CORS | Backend allows origins from env (`CORS_ORIGINS`). |
| Secrets | Use `.env` (not committed); set `DJANGO_SECRET_KEY` and strong `POSTGRES_PASSWORD` in production. |

## Optional: generate `poetry.lock`

From repo root (where `pyproject.toml` is):

```bash
poetry lock
```

Commit `poetry.lock` for reproducible Docker builds.
# Volleyball-marketing
# Volleyball-marketing
