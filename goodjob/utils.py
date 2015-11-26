import sys
from importlib import import_module
from contextlib import contextmanager

import six


def import_string(import_path):
    """Import a module path and return the module/attribute designated by
    the last name in the path. Raise ImportError if the import failed.
    """
    # The destination object is a module
    try:
        module = import_module(import_path)
    except ImportError:
        if '.' not in import_path:
            raise
    else:
        return module

    # The destination object is an attribute
    module_path, attr_name = import_path.rsplit('.', 1)
    module = import_module(module_path)
    try:
        return getattr(module, attr_name)
    except AttributeError:
        msg = (
            'No module named "{0}.{1}", nor does a module '
            'named "{0}" define a "{1}" attribute'.format(
                module_path, attr_name
            )
        )
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])


@contextmanager
def unbuffered():
    """A context manager that make stdout to be totally unbuffered."""
    original = sys.stdout

    # For the discussions of some possible solutions, see
    # http://stackoverflow.com/questions/107705/disable-output-buffering
    #
    # The following code works perfectly for jobs in Goodjob, since stdout
    # and stderr are actually redirected to the same log file for each job.
    #
    # TODO: Find a more general and standard solution
    sys.stdout = sys.stderr

    yield

    sys.stdout = original
