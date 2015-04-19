#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import shlex
import traceback
from subprocess import Popen, PIPE


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


class Command(object):
    def __init__(self, name):
        self.name = name
        self.process = None

    def cancel(self):
        self.process.terminate()

    def run(self, args='', **kwargs):
        kwargs['stdout'] = PIPE
        kwargs['stderr'] = PIPE
        cmd = shlex.split(self.name) + shlex.split(args)

        try:
            self.process = Popen(cmd, **kwargs)
        except OSError:
            msg = traceback.format_exc()
            raise CommandError(cmd, 1, msg)

        stdout_data, stderr_data = self.process.communicate()

        if self.process.returncode != 0:
            raise CommandError(cmd, self.process.returncode, stderr_data)

        sys.stdout.write(stdout_data)
