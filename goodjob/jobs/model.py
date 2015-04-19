#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from mongoengine import (
    Document, BooleanField,
    StringField, DateTimeField
)

from goodjob.config import config
from goodjob.constants import NOW


class JobEvent(object):
    started = 'started'
    finished = 'finished'
    failed = 'failed'
    cancelled = 'cancelled'


class JobStatus(object):
    pending = 'pending'
    in_progress = 'in_progress'
    finished = 'finished'
    failed = 'failed'
    cancelled = 'cancelled'


class Job(Document):
    meta = {'collection': config.COLLECTION_NAME}

    name = StringField(required=True)
    provider = StringField(required=True)
    notifier = StringField(default='goodjob-notifier')
    status = StringField(default=JobStatus.pending)
    schedule = StringField(default='')
    has_scheduled = BooleanField(default=False)
    date_created = DateTimeField(default=NOW)
    date_started = DateTimeField()
    date_stopped = DateTimeField()
    logfile = StringField(default='')
