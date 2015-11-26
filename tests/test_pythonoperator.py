#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
from goodjob.operators.python import PythonOperator
from .base import TestCase


def echo_ok(*args, **kwargs):
    print(args)
    print(kwargs)


def echo_err(*args, **kwargs):
    raise Exception('Some error occurs')


class TestPythonOperator(TestCase):

    def test_run_command_ok(self, capfd):
        operator = PythonOperator('tests.test_pythonoperator.echo_ok')
        operator.run(['arg1', 'arg2'])
        out, err = capfd.readouterr()
        assert err == "('arg1', 'arg2')\n{}\n"

    def test_run_command_err(self):
        operator = PythonOperator('tests.test_pythonoperator.echo_err')
        with pytest.raises(Exception) as exc:
            operator.run(['arg1', 'arg2'])
        expected_exc_part = 'Some error occurs'
        assert expected_exc_part in str(exc)
