# -*- coding: utf-8 -*-

from __future__ import absolute_import


class Manager(dict):

    def add(self, operator_class):
        self[operator_class.name] = operator_class

    def get_operator(self, operation):
        operator_class = self[operation.type]
        return operator_class(operation.command, operation.args,
                              **operation.kwargs)
