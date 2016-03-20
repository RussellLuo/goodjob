# -*- coding: utf-8 -*-

from __future__ import absolute_import


def notify(job_name, event):
    print('>>> job[%s] %s' % (job_name, event))
