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


# Connect MongoDB
# It may be strange to connect MongoDB here (in the configuration context),
# but this is the best place for ensuring that MongoDB is always connected.
from goodjob.db import connect
connect()
