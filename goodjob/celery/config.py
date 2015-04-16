#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

from goodjob.config import config
from .schedulers import DatabaseScheduler

BROKER_URL = config.REDIS_URL
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 30}
CELERY_RESULT_BACKEND = config.REDIS_URL
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYBEAT_SCHEDULER = DatabaseScheduler

CELERY_IMPORTS = (
	'goodjob.jobs.executor',
)
