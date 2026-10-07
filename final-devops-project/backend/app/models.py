from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from .database import Base

class DevOpsTask(Base):
    __tablename__ = "devops_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    session = Column(String(50), default="Session 21")
    status = Column(String(50), default="Completed")
    created_at = Column(DateTime, default=datetime.utcnow)
