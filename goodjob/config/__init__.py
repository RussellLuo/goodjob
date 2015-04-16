#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import default
from easyconfig import Config, envvar_object

config = Config()
config.from_object(default)
config.from_object(envvar_object('GOODJOB_SETTINGS_MODULE', silent=True))
