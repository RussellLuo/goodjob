#!/usr/bin/env python
# -*- coding: utf-8 -*-

# for MongoDB
MONGO_URL = 'mongodb://localhost:27017/'
DB_NAME = 'test'
COLLECTION_NAME = 'job'

# for Redis
REDIS_URL = 'redis://localhost:6379/0'

# for log file of jobs
LOGFILE_PATH = '/data/log/goodjob'

# for Celery
# maximum time (in seconds) to sleep between re-checking the schedule
CELERY_SCHEDULE_INTERVAL = 10
