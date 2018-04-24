from sqlalchemy import MetaData

from task.impl.input import Input
from task.impl.metadata import Metadata
from task.impl.task_base import TaskBase


class TestTask(TaskBase):
    r"""This is a test task"""

    def get_inputs(self):
        return []

    def run(self):
        pass