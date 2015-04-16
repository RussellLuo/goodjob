#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import subprocess

import click


@click.command()
@click.argument('event')
def main(event):
    args = ['echo', '>>> job %s' % event]
    return subprocess.call(args)


if __name__ == '__main__':
    main()
