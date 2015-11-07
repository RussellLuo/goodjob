#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

description = 'A service for executing asynchronous jobs.'

install_requires = [
    'celery==3.1.17',
    'redis==2.10.3',
    'restart-mongo',
    'mongoengine==0.9.0',
    'click==4.0',
]


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'goodjob/__init__.py')) as f:
        locals = {}
        exec(f.read(), locals)
        return locals['__version__']
    raise RuntimeError('No version info found.')


setup(
    name='Goodjob',
    version=get_version(),
    author='RussellLuo',
    author_email='luopeng.he@gmail.com',
    maintainer='RussellLuo',
    maintainer_email='luopeng.he@gmail.com',
    keywords='Asynchronous Job, Redis Queue, Python',
    description=description,
    license='MIT',
    long_description=description,
    packages=find_packages(exclude=['tests']),
    url='https://github.com/RussellLuo/goodjob',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'goodjob-executor = goodjob.cli.executor:main',
            'goodjob-notifier = goodjob.cli.notifier:main',
        ],
    },
)
