#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from restart.resource import Resource
from restart.exceptions import NotFound

from goodjob.api import api
from goodjob.jobs.model import Job


@api.route(uri='/jobs/<pk>/log', methods=['GET'])
class Log(Resource):
    name = 'log'

    def read(self, request, pk):
        job = Job.objects(id=pk).first()
        if job is None:
            raise NotFound('No job (%s) found' % pk)
        try:
            with open(job.logfile, 'r') as log:
                content = log.read()
                return content
        except IOError:
            raise NotFound('Log file (%s) missing' % job.logfile)
