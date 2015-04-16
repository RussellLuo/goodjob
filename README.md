Goodjob
=======

A service for executing asynchronous jobs.


Installation
------------

Install development version from `GitHub`:

    $ git clone https://github.com/RussellLuo/goodjob.git
    $ cd goodjob
    $ python setup.py install


Quickstart
----------

Start the API:

    $ gj-api

Start the celery worker:

    $ celery worker --app=goodjob.celery.app --loglevel=info

Start the celery scheduler (for periodic jobs):

    $ celery beat --app=goodjob.celery.app --loglevel=info

Create an one-off job:

    $ curl -i -X POST -H "Content-Type: application/json" -d '{
        "name": "greet",
        "provider": "echo hello"
    }' http://127.0.0.1:5000/jobs

or a periodic job (in crontab-style):

    $ curl -i -X POST -H "Content-Type: application/json" -d '{
        "name": "greet",
        "provider": "echo hello",
        "schedule": "* * * * * *"
    }' http://127.0.0.1:5000/jobs

Inspect the job:

    $ curl -i http://127.0.0.1:5000/jobs/<job-id>

See the job log:

    $ curl -i http://127.0.0.1:5000/logs/<job-id>
