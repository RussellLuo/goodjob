#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import errno
from subprocess import Popen, PIPE, STDOUT

from goodjob.config import config
from goodjob.celery.app import app as celery_app
from .model import Job


@celery_app.task(name='goodjob.core_job')
def core_job(job_id):
    job = Job.objects(id=job_id).first()
    executor = JobExecutor(job)
    executor.execute()


class JobExecutor(object):
    def __init__(self, job):
        self.job = job
        self.process = None

    def get_logfile(self):
        logfile_path = config.LOGFILE_PATH
        try:
            os.mkdir(logfile_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        logfile = os.path.join(logfile_path, '%s.log' % self.job.id)
        return logfile

    def execute(self):
        self.process = Popen(
            args=['gj-executor', str(self.job.id)],
            stdout=PIPE,
            stderr=STDOUT,
        )

        self.job.logfile = self.get_logfile()
        self.job.save()

        with open(self.job.logfile, 'w') as log:
            while self.process.poll() is None:
                data = self.process.stdout.read()
                log.write(data)

        return self.process.returncode
