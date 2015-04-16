#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import Flask
from rsrc.framework.flask import add_resource

from goodjob.jobs import jobs
from goodjob.logs import logs

app = Flask(__name__)

# attach resources to `app`
add_resource(app, jobs)
add_resource(app, logs)
