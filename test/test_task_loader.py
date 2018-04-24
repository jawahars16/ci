import logging
import os
from unittest import TestCase

from common.task_loader import TaskLoader


class TestTaskLoader(TestCase):

    def setUp(self):
        logging.getLogger().setLevel(logging.DEBUG)
        self.taskloader = TaskLoader(os.path.join(os.path.dirname(__file__).replace('test',''), 'task'))


    def test_load_tasks(self):
        tasks = self.taskloader.load_tasks('test')
        self.assertEqual(1, len(tasks))
        self.assertEqual(tasks[0].title, 'Test Task')
        self.assertEqual(tasks[0].description, 'This is a test task')