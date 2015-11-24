# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .manager import Manager
from .shell import ShellOperator
from .python import PythonOperator

manager = Manager()
manager.add(ShellOperator)
manager.add(PythonOperator)
