# -*- coding: utf-8 -*-

from __future__ import absolute_import

from restart.ext.crossdomain.cors import CORSMiddleware

from .config import config


class GoodjobCORSMiddleware(CORSMiddleware):
    """Override to change the default access-control options."""

    cors_allow_origin = config.CORS_ALLOW_ORIGIN
    cors_allow_credentials = config.CORS_ALLOW_CREDENTIALS
    cors_allow_methods = config.CORS_ALLOW_METHODS
    cors_allow_headers = config.CORS_ALLOW_HEADERS
    cors_max_age = config.CORS_MAX_AGE
