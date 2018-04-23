import logging
from unittest import TestCase

from service.task_service import TaskService

logging.getLogger().setLevel(logging.DEBUG)

class TestTask(TestCase):

    def test_get_all_tasks(self):
        service = TaskService()
        service.get_all_tasks()
