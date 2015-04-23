#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from . import default
from easyconfig import Config, yaml_mapping

config = Config()
config.from_object(default)

import os
yaml_filename = os.environ.get('GOODJOB_CONFIG_YAML', '')
config.from_mapping(yaml_mapping(yaml_filename, silent=True))
