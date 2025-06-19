python-recutils
===============

Python bindings for librec, the C library of GNU Recutils.

The build system now relies on ``setuptools``.  Install the bindings with::

    python -m pip install .

You can also use ``poetry`` to manage a development environment::

    poetry install

After installation run the test-suite using::

    python -m unittest

Or with ``poetry``::

    poetry run python -m unittest

For the manual type ``info python_recutils.info``.
