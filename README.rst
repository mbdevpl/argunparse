.. role:: bash(code)
    :language: bash

.. role:: python(code)
    :language: python


argunparse
==========

.. image:: https://img.shields.io/pypi/v/argunparse.svg
    :target: https://pypi.python.org/pypi/argunparse
    :alt: package version from PyPI

.. image:: https://travis-ci.org/mbdevpl/argunparse.svg?branch=master
    :target: https://travis-ci.org/mbdevpl/argunparse
    :alt: build status from Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/mbdevpl/argunparse?branch=master&svg=true
    :target: https://ci.appveyor.com/project/mbdevpl/argunparse
    :alt: build status from AppVeyor

.. image:: https://api.codacy.com/project/badge/Grade/fd6a7e9ac9324d9f9b5d1e77d10000e4
    :target: https://www.codacy.com/app/mbdevpl/argunparse
    :alt: grade from Codacy

.. image:: https://codecov.io/gh/mbdevpl/argunparse/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mbdevpl/argunparse
    :alt: test coverage from Codecov

.. image:: https://img.shields.io/pypi/l/argunparse.svg
    :target: https://github.com/mbdevpl/argunparse/blob/master/NOTICE
    :alt: license

The *argunparse* is intended to perform an approximate reverse of what *argparse* does. In short:
generating string of command-line arguments from a dict and/or a list.


how to use
----------

Simple example of how *argunparse* works:

.. code:: python

    import argunparse

    options = {
        'v': True,
        'long-flag': True,
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

for more examples see `<examples.ipynb>`_ notebook.


requirements
------------

Python >= 3.5.

No other runtime dependencies.

However, building and running tests requires packages listed in `<test_requirements.txt>`_.

Tested on Linux, OS X and Windows.


installation
------------

For simplest installation use :bash:`pip`:

.. code:: bash

    pip3 install argunparse

links
-----

-  *argparse*:

   https://docs.python.org/3/library/argparse.html
