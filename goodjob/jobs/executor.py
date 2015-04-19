#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import time
import errno
from subprocess import Popen

from goodjob.config import config
from goodjob.celery.app import app as celery_app
from .model import Job, JobStatus


@celery_app.task(name='goodjob.core_job')
def core_job(job_id):
    job = Job.objects(id=job_id).first()
    executor = JobExecutor(job)
    executor.execute()


class JobExecutor(object):
    def __init__(self, job):
        self.job = job
        self.process = None
        self.cancel_triggered = False

    def _get_logfile(self):
        logfile_path = config.LOGFILE_PATH
        try:
            os.mkdir(logfile_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        logfile = os.path.join(logfile_path, '%s.log' % self.job.id)
        return logfile

    def _is_job_cancelled(self):
        job = Job.objects(id=self.job.id).only('status').first()
        return job.status == JobStatus.cancelled

    def _cancel(self):
        self.process.terminate()

    def execute(self):
        self.job.logfile = self._get_logfile()
        self.job.save()

        with open(self.job.logfile, 'w') as log:
            self.process = Popen(
                args=['goodjob-executor', str(self.job.id)],
                stdout=log,
                stderr=log,
            )

            while True:
                if not self.cancel_triggered and self._is_job_cancelled():
                    self._cancel()
                    self.cancel_triggered = True
                if self.process.poll() is None:
                    time.sleep(0.1)
                else:
                    break

        return self.process.returncode
