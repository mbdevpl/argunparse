"""Initialization of tests of argunparse package."""

import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.WARNING)
logging.getLogger('argunparse').setLevel(logging.INFO)
