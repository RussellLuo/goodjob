#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

import click


@click.command()
@click.argument('event')
def main(event):
    args = ['echo', '>>> job %s' % event]
    return subprocess.call(args)


if __name__ == '__main__':
    main()
