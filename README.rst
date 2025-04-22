.. role:: bash(code)
    :language: bash

.. role:: python(code)
    :language: python


==========
argunparse
==========

Reversed argparse: generate string of command-line args from Python objects.

.. image:: https://img.shields.io/pypi/v/argunparse.svg
    :target: https://pypi.org/project/argunparse
    :alt: package version from PyPI

.. image:: https://github.com/mbdevpl/argunparse/actions/workflows/python.yml/badge.svg?branch=main
    :target: https://github.com/mbdevpl/argunparse/actions
    :alt: build status from GitHub

.. image:: https://codecov.io/gh/mbdevpl/argunparse/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/mbdevpl/argunparse
    :alt: test coverage from Codecov

.. image:: https://api.codacy.com/project/badge/Grade/fd6a7e9ac9324d9f9b5d1e77d10000e4
    :target: https://app.codacy.com/gh/mbdevpl/argunparse
    :alt: grade from Codacy

.. image:: https://img.shields.io/github/license/mbdevpl/argunparse.svg
    :target: NOTICE
    :alt: license

The *argunparse* is intended to perform an approximate reverse of what *argparse* does. In short:
generating string (or a list of strings) of command-line arguments from a dict and/or a list.

.. contents::
    :backlinks: none


How to use
==========

Simple example of how *argunparse* works:

.. code:: python

    import argunparse

    options = {
        'v': True,
        'long-flag': True,
        'ignored': False,
        'also-ignored': None,
        'o': 'out_file.txt',
        'log': 'log_file.txt'
        }
    args = {
        'in_file.txt'
        }

    unparser = argunparse.ArgumentUnparser()
    print(unparser.unparse(*args, **options))
    # -v --long-flag -o=out_file.txt --log=log_file.txt in_file.txt

    print(unparser.unparse_to_list(*args, **options))
    # ['-v', '--long-flag', '-o=out_file.txt', '--log=log_file.txt', 'in_file.txt']

Special option values are:

*   :python:`True` -- option will be treated as a flag;
*   :python:`False` and :python:`None` -- option will be ignored.

All other values will be converted to strings using :python:`str()`.

For more examples see `<examples.ipynb>`_ notebook.


Requirements
============

Python version 3.11 or later.

Python libraries as specified in `<requirements.txt>`_.

Building and running tests additionally requires packages listed in `<requirements_test.txt>`_.

Tested on Linux, macOS and Windows.


Installation
============

For simplest installation use :bash:`pip`:

.. code:: bash

    pip3 install argunparse

Links
=====

-  *argparse*:

   https://docs.python.org/3/library/argparse.html
