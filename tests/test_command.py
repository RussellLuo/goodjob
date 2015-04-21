#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

from goodjob.jobs.command import Command
from .base import TestCase

CUR_PATH = os.path.abspath(os.path.dirname(__file__))


class TestCommand(TestCase):
    def test_run_command_ok(self):
        cmd = Command('/bin/bash')
        script_name = os.path.join(CUR_PATH, 'wait_a_second.sh')
        cmd.run(script_name)
