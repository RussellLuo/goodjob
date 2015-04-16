#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rsrc import View, Response, status

from .model import Job
from . import executor


class JobView(View):
    def post(self, request):
        try:
            job = Job(**request.data)
            job.save()
        except Exception as e:
            errors = unicode(e)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        executor.execute(job.id)

        result = {'id': job.id, 'status': 'pending'}
        return Response(result, status=status.HTTP_201_CREATED)
