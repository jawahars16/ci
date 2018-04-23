from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from model.base import Base


class TaskParameter(Base):
    __tablename__ = 'task_parameter'

    id = Column(Integer, primary_key=True)
    step = Column(Integer, ForeignKey('step.id'), nullable=False)
    key = Column(String(50), nullable=False)
    value = Column(String(255))
    updated_on = Column(DateTime, default=datetime.utcnow())
