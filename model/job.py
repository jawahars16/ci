from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from model.base import Base
from model.step import Step


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50))
    steps = relationship('Step', lazy='select')
    created_on = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_on = Column(DateTime, default=datetime.utcnow())
