
==========
argunparse
==========

.. image:: https://img.shields.io/pypi/v/argunparse.svg
    :target: https://pypi.python.org/pypi/argunparse
    :alt: package version from PyPI

.. image:: https://travis-ci.org/mbdevpl/argunparse.svg?branch=master
    :target: https://travis-ci.org/mbdevpl/argunparse
    :alt: build status from Travis CI

.. image:: https://coveralls.io/repos/github/mbdevpl/argunparse/badge.svg?branch=master
    :target: https://coveralls.io/github/mbdevpl/argunparse?branch=master
    :alt: test coverage from Coveralls

.. image:: https://landscape.io/github/mbdevpl/argunparse/master/landscape.svg?style=flat
    :target: https://landscape.io/github/mbdevpl/argunparse/master
    :alt: code health from Landscape

.. image:: https://codeclimate.com/github/mbdevpl/argunparse/badges/gpa.svg
    :target: https://codeclimate.com/github/mbdevpl/argunparse
    :alt: code GPA from Code Climate

.. image:: https://codeclimate.com/github/mbdevpl/argunparse/badges/issue_count.svg
    :target: https://codeclimate.com/github/mbdevpl/argunparse
    :alt: issue count from Code Climate

.. image:: https://img.shields.io/pypi/l/argunparse.svg
    :alt: license

.. role:: bash(code)
    :language: bash

.. role:: python(code)
    :language: python

The *argunparse* is intended to perform an approximate reverse of what *argparse* does. In short:
generating string of command-line arguments from a dict and/or a list.


------------
requirements
------------

This package is intended for Python 3.5 and later. It was tested on 64 bit Ubuntu, but it might work
on other systems too.

------------
installation
------------

For simplest installation use :bash:`pip`:

.. code:: bash

    pip3.5 install argunparse

You can also build your own version:

.. code:: bash

    git clone https://github.com/mbdevpl/argunparse
    cd argunparse
    python3.5 -m unittest discover # make sure the tests pass
    python3.5 setup.py bdist_wheel
    ls -1tr dist/*.whl | tail -n 1 | xargs pip3.5 install


-----
usage
-----

Simple example of how *argunparse* works:

.. code:: python

    import argunparse

    flags = {
        'v': True,
        'long-flag': True,
        'o': 'out_file.txt',
        'log': 'log_file.txt'
        }
    args = {
        'in_file.txt'
        }

    unparser = argunparse.ArgumentUnparser()
    print(unparser.unparse_args(flags, args))

for more examples see :bash:`examples.ipynb` notebook.


-----
links
-----

-  *argparse*:

   https://docs.python.org/3/library/argparse.html
