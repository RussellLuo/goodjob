# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import traceback
from subprocess import Popen, PIPE

from .base import Operator


class CommandError(Exception):
    def __init__(self, cmd, retcode, stderr=None):
        self.cmd = cmd
        self.retcode = retcode
        self.stderr = stderr

    def __unicode__(self):
        return '`%s` returned %d:\nSTEDERR: %r' % (
            self.cmd, self.retcode, self.stderr
        )

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class ShellOperator(Operator):

    name = 'shell'

    def __init__(self, command, *args, **kwargs):
        super(ShellOperator, self).__init__(command, *args, **kwargs)
        self.process = None

    def cancel(self):
        self.process.terminate()

    def run(self, args=(), **kwargs):
        args, kwargs = self.merge_args(args, kwargs)

        kwargs['stdout'] = sys.stdout
        kwargs['stderr'] = PIPE
        cmd = [self.command] + args

        try:
            self.process = Popen(cmd, **kwargs)
        except OSError:
            msg = traceback.format_exc()
            raise CommandError(cmd, 1, msg)

        _, stderr_data = self.process.communicate()

        if self.process.returncode != 0:
            raise CommandError(cmd, self.process.returncode, stderr_data)
