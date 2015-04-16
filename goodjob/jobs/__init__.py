#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rsrc import Resource
from rsrc.contrib.db.mongo import serializer

from .view import JobView

jobs = Resource('jobs', JobView, serializer=serializer)
