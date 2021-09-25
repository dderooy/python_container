"""
To enable logging to syslog in your custom scripts,
add the following to the top of your python script:

    from docker-script import LOGGER

To use logging, you replace any "print" statements with
LOGGER.<LEVEL> where <LEVEL> can be:
    - debug
    - info
    - warning
    - error

So to log an error message, you would state:

    LOGGER.error("Some error message")

"""

import logging
import time

LOGGER = logging.getLogger('docker_script')
LOGGER.setLevel(logging.DEBUG)

HANDLER = logging.FileHandler('/script/logs/script_log.txt')

FORMATTER = logging.Formatter('%(asctime)s %(levelname)s [%(module)s.%(funcName)s]: %(message)s')
FORMATTER.converter = time.gmtime
HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(HANDLER)
