#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rsrc import View, Response
from rsrc.exceptions import NotFoundError

from goodjob.jobs.model import Job


class LogView(View):
    def get_item(self, request, pk):
        job = Job.objects(id=pk).first()
        try:
            with open(job.logfile, 'r') as log:
                content = log.read()
                return Response(content)
        except IOError:
            raise NotFoundError()
