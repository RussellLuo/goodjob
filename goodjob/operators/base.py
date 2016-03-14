# -*- coding: utf-8 -*-

from __future__ import absolute_import


class Operator(object):

    name = None

    def __init__(self, command, args=(), **kwargs):
        self.command = command
        self.args = args
        self.kwargs = kwargs

    def merge_args(self, args, kwargs):
        args = list(self.args) + list(args)
        kwargs = dict(self.kwargs.items() + kwargs.items())
        return args, kwargs

    def cancel(self):
        """Cancel the running command."""
        raise NotImplemented()

    def run(self, *args, **kwargs):
        """Run the command with arguments from `args` and `kwargs`."""
        raise NotImplemented()
