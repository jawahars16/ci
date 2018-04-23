from model.job import Job
from bootstrapper import db
import logging

from model.step import Step


class JobService:

    def add_job(self, title, description=None, job=None):

        if title is None:
            logging.warning('Title field is mandatory to add a job')
            return False

        job = Job(
            id=job,
            title=title,
            description=description
        )

        session = db.newSession()
        session.add(job)
        session.commit()
        session.close()

        return True

    def get_jobs(self):
        session = db.newSession()
        jobs = session.query(Job).all()
        session.close()
        return jobs

    def add_steps(self, job_id, steps):
        session = db.newSession()
        job = session.query(Job).get(job_id)

        if job is None:
            logging.error(f'Job with id {job_id} not found')
            return

        job.steps = steps
        session.merge(job)
        session.commit()
        session.close()

    def get_steps(self, job_id):
        session = db.newSession()
        steps = session.query(Step).filter_by(job=job_id).all()
        session.close()
        return steps
