#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import Celery


app = Celery('executor')
app.config_from_object('goodjob.celery.config')
