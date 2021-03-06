Goodjob
=======

A service for executing asynchronous jobs.


Installation
------------

Install `Goodjob` with `pip`:

    $ pip install Goodjob

Install development version from `GitHub`:

    $ git clone https://github.com/RussellLuo/goodjob.git
    $ cd goodjob
    $ python setup.py install


Quickstart
----------

### 1. Start databases

Start the MongoDB server (used by the Goodjob API):

    $ mongod

Start the Redis server (used by Celery):

    $ redis-server

### 2. Start services

Start the Goodjob API:

    $ restart goodjob.api:api

Start the Celery worker (only handles the `goodjob` queue):

    $ celery worker --app=goodjob.celery.app -Q goodjob --loglevel=info

Start the Celery scheduler (for periodic jobs):

    $ celery beat --app=goodjob.celery.app --loglevel=info

It is tedious to manage all the services by hand, you can ask the awesome `Supervisor` for help:

    $ supervisord -c ${GOODJOB_PROJ}/supervisord.conf
    $ supervisorctl -c ${GOODJOB_PROJ}/supervisord.conf status

### 3. Create jobs

Create an one-off job:

    $ curl -i -X POST -H "Content-Type: application/json" -d '{
        "name": "greet",
        "provider": {"type": "shell", "command": "echo", "args": ["hello"]}
    }' http://127.0.0.1:5000/jobs

or a periodic job (in crontab-style):

    $ curl -i -X POST -H "Content-Type: application/json" -d '{
        "name": "greet",
        "provider": {"type": "shell", "command": "echo", "args": ["hello"]},
        "schedule": "* * * * *"
    }' http://127.0.0.1:5000/jobs

Besides Shell jobs, Goodjob also supports Python jobs. A Python job is a Python callable specified by its Python path. For example:

    $ curl -i -X POST -H "Content-Type: application/json" -d '{
        "name": "email",
        "provider": {
            "type": "python",
            "command": "python_path.to.utility.send_email",
            "kwargs": {"to": "user@example.com", "subject": "Welcome", "body": "Hi there, buddy!"}
        }
    }' http://127.0.0.1:5000/jobs

Inspect the job:

    $ curl -i http://127.0.0.1:5000/jobs/<job-id>

See the job log:

    $ curl -i http://127.0.0.1:5000/jobs/<job-id>/log

### 4. Cancel jobs

Cancel a job (use [JSON Patch][1] syntax):

    $ curl -i -X PATCH -H "Content-Type: application/json" -d '[{
        "op": "add",
        "path": "/status",
        "value": "cancelled"
    }]' http://127.0.0.1:5000/jobs/<job-id>

### 5. Delete jobs

Delete a job:

    $ curl -i -X DELETE http://127.0.0.1:5000/jobs/<job-id>


License
-------

[MIT][2]


[1]: http://tools.ietf.org/html/rfc6902
[2]: http://opensource.org/licenses/MIT
