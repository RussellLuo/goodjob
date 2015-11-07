from __future__ import absolute_import

from restart.serving import Service

from goodjob.api import api


application = Service(api)
