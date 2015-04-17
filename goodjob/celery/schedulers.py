#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from bson import ObjectId
from celery.beat import ScheduleEntry, PersistentScheduler
from celery.schedules import crontab

from goodjob.config import config
from goodjob.jobs.model import Job


class DatabaseScheduler(PersistentScheduler):
    """Job scheduler based on database."""

    def __init__(self, *args, **kwargs):
        # force `self.schedule` to be initialized
        kwargs['lazy'] = False
        super(DatabaseScheduler, self).__init__(*args, **kwargs)

        # this scheduler must wake up more frequently than the
        # regular of 5 minutes because it needs to take external
        # changes to the schedule into account.
        self.max_interval = config.CELERY_SCHEDULE_INTERVAL

        # schedule all periodic jobs from database for the first time
        self.update_schedule(forced=True)

    def update_schedule(self, forced=False):
        """Update schedule entries for periodic jobs."""

        condition = dict(schedule__ne='')
        if not forced:
            condition.update(has_scheduled=False)

        # remove entries for jobs that have been deleted
        deleted_entriy_ids = [
            entry_id
            for entry_id in self.schedule
            if Job.objects(id=ObjectId(entry_id)).first() is None
        ]
        for entry_id in deleted_entriy_ids:
            self.remove_entry(entry_id)

        # add/update entries for jobs that have not been scheduled
        for job in Job.objects(**condition):
            args = job.schedule.split()
            schedule = crontab(*args)
            self.schedule[str(job.id)] = ScheduleEntry(
                app=self.app,
                name=str(job.id),
                schedule=schedule,
                task='goodjob.core_job',
                args=[job.id],
            )

            job.has_scheduled = True
            job.save()

    def tick(self):
        """Override to schedule newcome periodic jobs."""
        self.update_schedule()
        return super(DatabaseScheduler, self).tick()

    def remove_entry(self, entry_id):
        entry_id = str(entry_id)
        if entry_id in self.schedule:
            del self.schedule[entry_id]
