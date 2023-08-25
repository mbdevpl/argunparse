"""Initialization of tests of argunparse package."""

import boilerplates.logging


class TestsLogging(boilerplates.logging.Logging):
    """Logging configuration for tests."""

    packages = ['argunparse']


TestsLogging.configure()
