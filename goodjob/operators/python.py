# -*- coding: utf-8 -*-

from __future__ import absolute_import

from goodjob.utils import import_string, unbuffered
from .base import Operator


class PythonOperator(Operator):

    name = 'python'

    def __init__(self, command, *args, **kwargs):
        super(PythonOperator, self).__init__(command, *args, **kwargs)
        self.callable = import_string(self.command)

    def cancel(self):
        pass

    def run(self, args=(), **kwargs):
        args, kwargs = self.merge_args(args, kwargs)
        with unbuffered():
            self.callable(*args, **kwargs)
