#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys

import click

from goodjob.jobs.model import Job, JobStatus, JobEvent
from goodjob.jobs.command import Command
from goodjob.constants import NOW


@click.command()
@click.argument('job_id')
def main(job_id):
    job = Job.objects(id=job_id).first()
    provider = Command(job.provider)
    notifier = Command(job.notifier)

    notifier.run(JobEvent.started)
    job.status = JobStatus.in_progress
    job.date_started = NOW()
    job.save()
    try:
        provider.run()
    except Exception as e:
        sys.stderr.write(unicode(e))
        notifier.run(JobEvent.failed)
        job.status = JobStatus.failed
    else:
        notifier.run(JobEvent.finished)
        job.status = JobStatus.finished
    job.date_stopped = NOW()
    job.save()


if __name__ == '__main__':
    main()
