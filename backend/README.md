# Portal22 Backend

FastAPI + SQLAlchemy backend with basic auth scaffolding.

## Quickstart

```bash
# From repo root
python -m venv venv
./venv/Scripts/Activate.ps1  # PowerShell
pip install -r backend/requirements.txt -r backend/requirements-dev.txt

# Run tests
pytest -q

# Start server
uvicorn app.main:app --reload
```

## Environment
Configure env via `.env` or system env:
- `SECRET_KEY` (string)
- `DATABASE_URL` (e.g., `sqlite:///./backend/app/app.db`)
- `ACCESS_TOKEN_EXPIRE_MINUTES` (int)

## Migrations
Autogenerate + apply:
```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```
