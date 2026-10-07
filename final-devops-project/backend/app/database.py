import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgrespassword")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "devops_db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Fallback mechanism if postgres isn't running locally during manual run testing
db_connected = False
engine = None
SessionLocal = None

try:
    engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 3})
    with engine.connect() as conn:
        db_connected = True
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception:
    # Use SQLite in-memory fallback for local manual demonstration if Postgres is offline
    fallback_url = "sqlite:///./devops_local.db"
    engine = create_engine(fallback_url, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_connected = False

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_db_health():
    global db_connected
    try:
        with engine.connect() as conn:
            return {"status": "connected", "type": "PostgreSQL" if "postgresql" in str(engine.url) else "SQLite fallback", "host": DB_HOST, "port": DB_PORT}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)}
