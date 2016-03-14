#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

import pytest
from goodjob.operators.shell import ShellOperator, CommandError
from .base import TestCase

CUR_PATH = os.path.abspath(os.path.dirname(__file__))
SCRIPT_NAME = os.path.join(CUR_PATH, 'wait_a_second.sh')


class TestShellOperator(TestCase):

    def test_run_command_ok(self, capfd):
        operator = ShellOperator('/bin/bash')
        operator.run(SCRIPT_NAME)
        out, err = capfd.readouterr()
        assert out == 'start...\nwait...\nwait...\nwait...\nend...\n'

    def test_run_command_err(self):
        operator = ShellOperator('/bin/non-bash')
        with pytest.raises(CommandError) as exc:
            operator.run(SCRIPT_NAME)
        expected_exc_part = (
            "CommandError: `['/bin/non-bash', '%s']`" % SCRIPT_NAME
        )
        assert expected_exc_part in str(exc)
