impulsare/logger
===============================

.. image:: https://travis-ci.org/impulsare/logger.svg?branch=master
    :target: https://travis-ci.org/impulsare/logger

.. image:: https://scrutinizer-ci.com/g/impulsare/logger/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/impulsare/logger/

.. image:: https://scrutinizer-ci.com/g/impulsare/logger/badges/coverage.png?b=master
    :target: https://travis-ci.org/impulsare/logger


Overview
--------------------

A logger that sends its logs to rotated files + directly to console (configurable).


Installation / Usage
--------------------

To install use pip:

.. code-block:: bash

    $ pip install --upgrade impulsare-logger



Configuration
--------
To be able to use the logger you need to create a configuration file
that contains the following parameters:

.. code-block:: yaml

    logger:
         # Where to store the logs. The file is generated by a parameter
         # Set on Class Init
        directory: /var/log
         # CRITICAL, ERROR, WARNING, INFO, DEBUG
        level: WARNING
        # Optional for files, see https://docs.python.org/3/library/logging.html#logging.Formatter
        formatter: '%(asctime)s :: %(levelname)s :: %(message)s'
        # In MB, before rotating
        max_size: 10
        # How many files to keep
        rotate: 3
        # Where to log ?
        handlers:
            console: false
            file: true


Example
-------

.. code-block:: python

    from impulsare_logger import Logger


    logger = Logger('app', 'tests/static/config_valid.yml')
    logger.log.warning('coucou')



Tests
--------

.. code-block:: bash

    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ py.test
