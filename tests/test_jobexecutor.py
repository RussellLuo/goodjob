#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import time

from goodjob.jobs.models import Job, JobStatus
from goodjob.jobs.executor import JobExecutor
from .base import TestCase


class TestJobExecutor(TestCase):
    def test_execute_job(self):
        job = self.create_job()

        # execute the job
        executor = JobExecutor(job)
        async_job = self.apply_async(executor.execute)
        async_job.start()

        async_job.join()
        job = Job.objects(id=job.id).first()
        assert(job.status == JobStatus.finished)
        assert(job.date_started is not None)
        assert(job.date_stopped is not None)

        with open(job.logfile, 'r') as log:
            text = log.read()
            assert('>>> job finished' in text)

    def test_cancel_job(self):
        job = self.create_job(command='sleep 30')
        executor = JobExecutor(job)
        async_job = self.apply_async(executor.execute)
        async_job.start()

        # wait for the job to actually start running
        time.sleep(1)

        # cancel the job
        job.status = JobStatus.cancelled
        job.save()

        async_job.join()
        job = Job.objects(id=job.id).first()
        assert(job.status == JobStatus.cancelled)
        assert(job.date_started is not None)
        assert(job.date_stopped is not None)

        with open(job.logfile, 'r') as log:
            text = log.read()
            assert('>>> job cancelled' in text)
