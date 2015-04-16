#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongoengine

from config import config


def connect():
    mongoengine.connect(config.DB_NAME, host=config.MONGO_URL)
