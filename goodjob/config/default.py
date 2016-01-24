# -*- coding: utf-8 -*-

# For MongoDB
MONGO_URL = 'mongodb://localhost:27017/'
DB_NAME = 'test'
COLLECTION_NAME = 'job'

# For Redis
REDIS_URL = 'redis://localhost:6379/0'

# For log file of jobs
LOGFILE_PATH = '/data/log/goodjob'

# For Celery
# maximum time (in seconds) to sleep between re-checking the schedule
CELERY_SCHEDULE_INTERVAL = 10

# For CORS
CORS_ALLOW_ORIGIN = '*'  # any domain
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')
CORS_ALLOW_HEADERS = ()  # any headers
CORS_MAX_AGE = 864000  # 10 days
