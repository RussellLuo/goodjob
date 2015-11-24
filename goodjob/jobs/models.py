#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from mongoengine import (
    Document, EmbeddedDocument,
    EmbeddedDocumentField,
    BooleanField, StringField,
    DateTimeField, ListField, DictField
)

from goodjob.config import config
from goodjob.constants import NOW
from goodjob.operators import manager


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


class Operation(EmbeddedDocument):
    type = StringField(required=True, choices=manager.keys())
    command = StringField(required=True)
    args = ListField()
    kwargs = DictField()


def default_notifier():
    return Operation(type='shell', command='goodjob-notifier')


class Job(Document):
    meta = {'collection': config.COLLECTION_NAME}

    name = StringField(required=True)
    provider = EmbeddedDocumentField(Operation)
    notifier = EmbeddedDocumentField(Operation, default=default_notifier)
    status = StringField(default=JobStatus.pending)
    schedule = StringField(default='')
    has_scheduled = BooleanField(default=False)
    date_created = DateTimeField(default=NOW)
    date_started = DateTimeField()
    date_stopped = DateTimeField()
    logfile = StringField(default='')
    description = StringField(default='')
