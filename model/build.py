from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from model.base import Base
from datetime import datetime


class Build(Base):

    __tablename__ = 'build'

    id = Column(String(50), primary_key=True, autoincrement=False)
    job = Column(Integer, ForeignKey('job.id'), nullable=False)
    status = Column(Integer, nullable=False)
    initiated_on = Column(DateTime, nullable=False,
                          default=datetime.utcnow())
    initiated_by = Column(String(50))
