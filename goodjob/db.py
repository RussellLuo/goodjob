#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import mongoengine

from goodjob.config import config


def connect():
    mongoengine.connect(config.DB_NAME, host=config.MONGO_URL)
