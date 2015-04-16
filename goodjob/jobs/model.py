#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import (
    Document, StringField, DateTimeField
)

from goodjob.constants import NOW


class JobEvent(object):
    started = 'started'
    finished = 'finished'
    failed = 'failed'


class JobStatus(object):
    pending = 'pending'
    in_progress = 'in_progress'
    finished = 'finished'
    failed = 'failed'


class Job(Document):
    name = StringField(required=True)
    provider = StringField(required=True)
    notifier = StringField(default='gj-notifier')
    status = StringField(default=JobStatus.pending)
    date_created = DateTimeField(default=NOW)
    date_started = DateTimeField()
    date_stopped = DateTimeField()
    logfile = StringField(default='')
