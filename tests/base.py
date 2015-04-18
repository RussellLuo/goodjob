#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

from goodjob.jobs.model import Job


class TestCase(object):
    def create_job(self, name='test', provider='echo test'):
        job = Job(name=name, provider=provider)
        job.save()
        return job

    def apply_async(self, func):
        d = threading.Thread(target=func)
        d.setDaemon(True)
        return d
