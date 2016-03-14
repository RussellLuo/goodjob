#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import subprocess

import click


@click.command()
@click.argument('job_name')
@click.argument('event')
def main(job_name, event):
    args = ['echo', '>>> job[%s] %s' % (job_name, event)]
    return subprocess.call(args)


if __name__ == '__main__':
    main()
