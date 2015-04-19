#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import signal

import click

from goodjob.jobs.model import Job, JobStatus, JobEvent
from goodjob.jobs.command import Command
from goodjob.constants import NOW


class RealJobExecutor(object):
    def __init__(self, job):
        self.job = job
        self.provider = Command(job.provider)
        self.notifier = Command(job.notifier)

        # register the handler of signal SIGTERM
        signal.signal(signal.SIGTERM, self.sigterm_received)

    def sigterm_received(self, signum, stack):
        # cancel the provider process
        self.provider.cancel()

        self.notifier.run(JobEvent.cancelled)
        self.job.status = JobStatus.cancelled
        self.job.date_stopped = NOW()
        self.job.save()

        # exit explicitly (raise `SystemExit`)
        sys.exit(1)

    def execute(self):
        self.notifier.run(JobEvent.started)
        self.job.status = JobStatus.in_progress
        self.job.date_started = NOW()
        self.job.save()

        try:
            self.provider.run()
        # do not use `except:` here,
        # since we do not want to catch `SystemExit`
        except Exception as e:
            sys.stderr.write(unicode(e))
            self.notifier.run(JobEvent.failed)
            self.job.status = JobStatus.failed
        else:
            self.notifier.run(JobEvent.finished)
            self.job.status = JobStatus.finished
        self.job.date_stopped = NOW()
        self.job.save()


@click.command()
@click.argument('job_id')
def main(job_id):
    job = Job.objects(id=job_id).first()
    executor = RealJobExecutor(job)
    executor.execute()


if __name__ == '__main__':
    main()
