#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rsrc import Resource

from .view import LogView

logs = Resource('logs', LogView)
