#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from rsrc import Response, status
from rsrc.contrib.db.mongo import Collection

from goodjob.celery.app import app as celery_app
from .model import Job

# connect MongoDB
from goodjob.db import connect
connect()


class JobView(Collection):
    def __init__(self, *args, **kwargs):
        kwargs.update(db=Job._get_db(), table_name=Job._get_collection_name())
        super(JobView, self).__init__(*args, **kwargs)

    def post(self, request):
        try:
            job = Job(**request.data)
            job.save()
        except Exception as e:
            errors = unicode(e)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        # queue non-periodic jobs at once
        if not job.schedule:
            celery_app.send_task("goodjob.core_job", [job.id])

        result = {'id': job.id, 'status': 'pending'}
        return Response(result, status=status.HTTP_201_CREATED)
