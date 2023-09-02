"""Initialization of tests of argunparse package."""

import logging

import boilerplates.logging


class TestsLogging(boilerplates.logging.Logging):
    """Logging configuration for tests."""

    packages = ['argunparse']


TestsLogging.configure()
logging.getLogger('argunparse.argument_unparser').setLevel(logging.INFO)
