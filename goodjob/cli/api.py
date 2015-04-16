#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from goodjob.app import app


@click.command()
@click.option('--host', '-h', default='127.0.0.1')
@click.option('--port', '-p', default=5000)
@click.option('--debug', '-d', default=False)
def main(host, port, debug):
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
