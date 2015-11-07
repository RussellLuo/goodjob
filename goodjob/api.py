#!/usr/bin/env python
# -*- coding: utf-8 -*-

from restart.api import RESTArt
from restart.utils import load_resources


api = RESTArt()


# Load all resources
load_resources(['goodjob.jobs.resource', 'goodjob.logs.resource'])
