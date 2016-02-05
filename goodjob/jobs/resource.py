# -*- coding: utf-8 -*-

from __future__ import absolute_import

from restart import status
from restart.utils import make_location_header
from restart.ext.mongo.collection import Collection

from goodjob.api import api
from goodjob.cors import GoodjobCORSMiddleware
from goodjob.celery.app import app as celery_app
from .models import Job


@api.register
class Jobs(Collection):
    name = 'jobs'

    database = Job._get_db()
    collection_name = Job._get_collection_name()

    middleware_classes = (
        (GoodjobCORSMiddleware,) + Collection.middleware_classes
    )

    def create(self, request):
        try:
            job = Job(**request.data)
            job.save()
        except Exception as e:
            errors = unicode(e)
            return errors, status.HTTP_400_BAD_REQUEST

        # Queue non-periodic jobs at once
        if not job.schedule:
            celery_app.send_task('goodjob.core_job', [job.id], queue=job.queue)

        result = {'id': job.id, 'status': 'pending'}
        headers = {'Location': make_location_header(request, job.id)}
        return result, status.HTTP_201_CREATED, headers
