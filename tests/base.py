#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shlex
from multiprocessing import Process

from goodjob.jobs.models import Job, Operation


class TestCase(object):
    def create_job(self, name='test', command='echo test'):
        args = shlex.split(command)
        provider = Operation(type='shell', command=args[0], args=args[1:])
        job = Job(name=name, provider=provider)
        job.save()
        return job

    def apply_async(self, func, args=()):
        proc = Process(target=func, args=args)
        proc.daemon = True
        return proc
