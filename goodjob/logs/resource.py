#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from restart.resource import Resource
from restart.exceptions import NotFound

from goodjob.api import api
from goodjob.jobs.model import Job


@api.register
class Logs(Resource):
    name = 'logs'

    def read(self, request, pk):
        job = Job.objects(id=pk).first()
        try:
            with open(job.logfile, 'r') as log:
                content = log.read()
                return content
        except IOError:
            raise NotFound()
