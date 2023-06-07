from config.settings.base import *  # noqa

import logging
import sys

DEFAULT_FROM_EMAIL = "webmaster@localhost"

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    logging.disable(logging.CRITICAL)