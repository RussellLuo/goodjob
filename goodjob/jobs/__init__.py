#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from rsrc import Resource
from rsrc.contrib.db.mongo import serializer

from .view import JobView

jobs = Resource('jobs', JobView, serializer=serializer)
