#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongoengine
from redis import Redis

from config import config

mongo_url = 'mongodb://{host}:{port}/'.format(
    host=config.MONGO_HOST, port=config.MONGO_PORT
)
MONGO_CONN = mongoengine.connect(config.DB_NAME, host=mongo_url)

REDIS_CONN = Redis(config.REDIS_HOST, config.REDIS_PORT)
