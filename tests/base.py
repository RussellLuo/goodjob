#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process

from goodjob.jobs.model import Job


class TestCase(object):
    def create_job(self, name='test', provider='echo test'):
        job = Job(name=name, provider=provider)
        job.save()
        return job

    def apply_async(self, func, args=()):
        proc = Process(target=func, args=args)
        proc.daemon = True
        return proc
