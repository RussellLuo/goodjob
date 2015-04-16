#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery.beat import ScheduleEntry, PersistentScheduler
from celery.schedules import crontab

from goodjob.jobs.model import Job


# This scheduler must wake up more frequently than the
# regular of 5 minutes because it needs to take external
# changes to the schedule into account.
DEFAULT_MAX_INTERVAL = 5  # seconds


class DatabaseScheduler(PersistentScheduler):
    """Job scheduler based on database."""

    def __init__(self, *args, **kwargs):
        # force `self._store` to be initialized
        kwargs['lazy'] = False
        super(DatabaseScheduler, self).__init__(*args, **kwargs)

        self.max_interval = DEFAULT_MAX_INTERVAL

        # read periodic jobs from database for the first time
        self.update_schedule(forced=True)

    def update_schedule(self, forced=False):
        conditon = dict(schedule__ne='')
        if not forced:
            conditon.update(has_scheduled=False)

        for job in Job.objects(**conditon):
            args = job.schedule.split()
            schedule = crontab(*args)
            self._store['entries'][str(job.id)] = ScheduleEntry(
                app=self.app,
                name=job.name,
                schedule=schedule,
                task='goodjob.core_job',
                args=[job.id],
            )

            job.has_scheduled = True
            job.save()

    def tick(self):
        self.update_schedule()
        return super(DatabaseScheduler, self).tick()
