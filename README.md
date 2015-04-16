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

Start the worker:

    $ gj-worker high

Provide a job:

    $ curl -i -X POST -H "Content-Type: application/json" -d '{
        "name": "greet",
        "provider": "echo hello"
    }' http://127.0.0.1:5000/jobs

See the job result:

    $ curl -i http://127.0.0.1:5000/logs/<job-id>
