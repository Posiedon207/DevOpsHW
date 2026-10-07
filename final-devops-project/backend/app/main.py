import time
import os
import platform
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

from .database import engine, Base, get_db, check_db_health
from .models import DevOpsTask

# Create tables
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Warning: Tables creation deferred: {e}")

app = FastAPI(
    title="DevOps 3-Tier Application API",
    description="Backend microservice for DevOps Course Session 21 assignment (FastAPI + PostgreSQL + Prometheus Metrics)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for frontend on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus Metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests", ["method", "endpoint", "status_code"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "HTTP Request Latency", ["endpoint"])
APP_UPTIME = Gauge("app_uptime_seconds", "Application Uptime in Seconds")
START_TIME = time.time()

# Seed initial tasks if empty
def init_seed_data():
    try:
        from .database import SessionLocal
        db = SessionLocal()
        if db.query(DevOpsTask).count() == 0:
            sample_tasks = [
                DevOpsTask(title="Session 21: Full Application Stack Run", description="Manual deployment of Frontend, Backend and Postgres DB", session="Session 21", status="Completed"),
                DevOpsTask(title="Session 21: Containerization with Dockerfiles", description="Build Dockerfile for frontend and backend", session="Session 21", status="Completed"),
                DevOpsTask(title="Session 21: Multi-Container Orchestration", description="Deploy full stack with docker-compose up -d --build", session="Session 21", status="Completed"),
                DevOpsTask(title="Session 21: API & Monitoring Validation", description="Verify /docs, /health, and /metrics endpoints", session="Session 21", status="Completed"),
            ]
            db.add_all(sample_tasks)
            db.commit()
        db.close()
    except Exception as e:
        print(f"Seed note: {e}")

init_seed_data()

# Middleware for metrics tracking
@app.middleware("http")
async def monitor_requests(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    
    endpoint = request.url.path
    method = request.method
    status_code = str(response.status_code)
    
    REQUEST_COUNT.labels(method=method, endpoint=endpoint, status_code=status_code).inc()
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
    APP_UPTIME.set(time.time() - START_TIME)
    
    return response

# Pydantic Schemas
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    session: Optional[str] = "Session 21"
    status: Optional[str] = "Pending"

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    session: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

# --- Endpoints ---

@app.get("/", summary="Root Status Endpoint")
def read_root():
    """Welcome endpoint for DevOps backend service"""
    return {
        "project": "DevOps 3-Tier Web Application",
        "session": "Session 21",
        "author": "posiedon2212@gmail.com",
        "status": "online",
        "framework": "FastAPI",
        "documentation": "/docs",
        "health_check": "/health",
        "metrics": "/metrics"
    }

@app.get("/health", summary="Application Health Check")
def health_check():
    """Health check endpoint verifying backend and PostgreSQL connectivity"""
    db_info = check_db_health()
    uptime_sec = round(time.time() - START_TIME, 2)
    return {
        "status": "healthy",
        "service": "devops-backend-api",
        "environment": os.getenv("APP_ENV", "production"),
        "uptime_seconds": uptime_sec,
        "database": db_info,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "version": "1.0.0"
    }

@app.get("/metrics", summary="Prometheus Metrics Endpoint")
def get_metrics():
    """Endpoint scraped by Prometheus for cluster and service monitoring"""
    APP_UPTIME.set(time.time() - START_TIME)
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/api/tasks", response_model=List[TaskResponse], summary="List All DevOps Tasks")
def get_tasks(db: Session = Depends(get_db)):
    """Fetch all tasks from the database"""
    try:
        tasks = db.query(DevOpsTask).all()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED, summary="Create a DevOps Task")
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    """Add a new task to PostgreSQL"""
    try:
        new_task = DevOpsTask(
            title=task_in.title,
            description=task_in.description,
            session=task_in.session,
            status=task_in.status
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/system", summary="System Information")
def system_info():
    """Return runtime host and environment metadata"""
    return {
        "hostname": platform.node(),
        "system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "container_id": os.getenv("HOSTNAME", "local-dev"),
        "db_host": os.getenv("DB_HOST", "localhost"),
        "port": 8000
    }
