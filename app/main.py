import logging
import os

import psycopg2
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
def startup_event() -> None:
    """Attempt a simple database connection on startup."""
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        logging.warning("DATABASE_URL not set; skipping DB connection test")
        return
    try:
        with psycopg2.connect(dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
        logging.info("Successfully connected to the database")
    except Exception as exc:  # pragma: no cover - simple logging
        logging.error("Database connection failed: %s", exc)


@app.get("/")
def read_root() -> dict[str, str]:
    """Basic sanity endpoint."""
    return {"message": "Time Tracking Assistant API"}
