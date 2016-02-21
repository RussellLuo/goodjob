# -*- coding: utf-8 -*-

from __future__ import absolute_import

from easyconfig import Config, yaml_mapping

from . import default


config = Config(default)

# Override the default configuration if `GOODJOB_CONFIG_YAML` is given
config.load(yaml_mapping('GOODJOB_CONFIG_YAML', silent=True, is_envvar=True))


# Connect MongoDB
# It may be strange to connect MongoDB here (in the configuration context),
# but this is the best place for ensuring that MongoDB is always connected.
from goodjob.db import connect
connect()
