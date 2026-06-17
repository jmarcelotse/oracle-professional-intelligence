"""Conexão com PostgreSQL via pool psycopg3.

Lê configuração do ambiente (ver .env.example). Mantém um ConnectionPool
global reutilizado pelas rotas.
"""
import os
from contextlib import contextmanager

from psycopg_pool import ConnectionPool

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_NAME = os.getenv("DATABASE_NAME", "oracle_professional_intelligence")
DATABASE_USER = os.getenv("DATABASE_USER", "oracle")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "oracle")

CONNINFO = (
    f"host={DATABASE_HOST} port={DATABASE_PORT} dbname={DATABASE_NAME} "
    f"user={DATABASE_USER} password={DATABASE_PASSWORD}"
)

# open=False: o pool só abre conexões quando usado, evitando crash no boot
# caso o banco ainda não esteja pronto.
pool = ConnectionPool(CONNINFO, min_size=1, max_size=5, open=False, timeout=5)


def ensure_open() -> None:
    if pool.closed:
        pool.open()


@contextmanager
def cursor(row_factory=None):
    ensure_open()
    with pool.connection() as conn:
        with conn.cursor(row_factory=row_factory) as cur:
            yield cur


def check() -> bool:
    """Retorna True se o banco responde a um SELECT 1."""
    try:
        with cursor() as cur:
            cur.execute("SELECT 1")
            cur.fetchone()
        return True
    except Exception:
        return False
