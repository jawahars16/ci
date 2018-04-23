from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from model.base import Base
import model.job
import model.step


class Database:
    def __init__(self, path, echo=False):
        self.engine = create_engine(path, poolclass=NullPool)
        self.engine.echo = echo
        self.session = sessionmaker(bind=self.engine)

    def create(self):
        Base.metadata.create_all(self.engine)

    def newSession(self):
        return self.session()

    def dropAll(self):
        Base.metadata.drop_all(self.engine)
