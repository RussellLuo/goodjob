#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from rsrc import Resource

from .view import LogView

logs = Resource('logs', LogView)
