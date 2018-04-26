from sqlalchemy import MetaData

from task.impl.input import Input
from task.impl.metadata import Metadata
from task.impl.task_base import TaskBase


class TestTask(TaskBase):
    r"""This is a test task"""

    def get_inputs(self):
        test_input_1 = Input('test1', 'Test 1', 'text', '', True)
        test_input_2 = Input('test2', 'Test 2', 'text', '', False)
        return [test_input_1, test_input_2]

    def run(self):
        pass