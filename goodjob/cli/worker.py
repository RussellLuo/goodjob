#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

import click


@click.command()
@click.argument('args', nargs=-1)
def main(args):
    args = ['rqworker'] + list(args[:])
    return subprocess.call(args)


if __name__ == '__main__':
    main()
