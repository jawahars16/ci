from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from model.task_parameter import TaskParameter
from model.base import Base


class Step(Base):
    __tablename__ = 'step'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    job = Column(Integer, ForeignKey('job.id'), nullable=False)
    parameters = relationship('TaskParameter', lazy='select')

    def __init__(self, title, job_id):
        self.title = title
        self.job = job_id
