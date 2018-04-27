import os
from unittest import TestCase
import logging
from datacontext.database import Database
from model.job import Job
from model.step import Step
from model.task_parameter import TaskParameter
from service.job_service import JobService


class TestJob(TestCase):

    def setUp(self):
        self.testdb = Database('sqlite:///test/data/database.db')
        logging.getLogger().setLevel(logging.DEBUG)

    def tearDown(self):
        pass
        self.testdb.dropAll()

    def test_add_job(self):
        service = JobService(self.testdb)
        service.add_job('Test title', 'Test description')

        jobs = service.get_jobs()
        self.assertEqual(1, len(jobs))
        self.assertEqual(jobs[0].title, 'Test title')

    def test_add_job_without_title(self):
        service = JobService(self.testdb)
        service.add_job(None)

        jobs = service.get_jobs()
        self.assertEqual(0, len(jobs))

    def test_add_steps_to_job(self):
        service = JobService(self.testdb)
        service.add_job('Test title', 'Test description')

        jobs = service.get_jobs()
        job_id = jobs[0].id

        step1_parameter1 = TaskParameter(
            key='step1_key1', value='step1_value1')
        step1_parameter2 = TaskParameter(
            key='step1_key2', value='step1_value2')

        step1 = Step('Test step 1', job_id)
        step1.parameters = [step1_parameter1, step1_parameter2]

        step2_parameter1 = TaskParameter(
            key='step2_key1', value='step2_value1')
        step2_parameter2 = TaskParameter(
            key='step2_key2', value='step2_value2')
        step2_parameter3 = TaskParameter(
            key='step2_key3', value='step2_value3')

        step2 = Step('Test step 2', job_id)
        step2.parameters = [step2_parameter1,
                            step2_parameter2, step2_parameter3]

        service.add_steps(job_id, [step1, step2])

        steps = service.get_steps(job_id)
        self.assertEqual(2, len(steps))
        self.assertEqual('Test step 1', steps[0].title)
