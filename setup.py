"""This is "setup.py" file for "argunparse"."""

import os
import shutil
import sys
import typing

import setuptools

from argunparse._version import VERSION as version

_HERE = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
_SRC_DIR = '.'

def clean():
    if os.path.isdir('build'):
        shutil.rmtree('build')

def long_description() -> str:
    """ Read contents of README.rst file and return them. """

    desc = ''
    with open(os.path.join(_HERE, 'README.rst'), encoding='utf-8') as f:
        desc = f.read()
    return desc

def classifiers() -> typing.List[str]:
    """
    Project classifiers.

    See: https://pypi.python.org/pypi?:action=list_classifiers
    """

    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
        ]
    return classifiers

def packages() -> typing.List[str]:
    """ Find packages to pack. """

    exclude = ['test', 'test.*'] if 'bdist_wheel' in sys.argv else ()
    packages = setuptools.find_packages(_SRC_DIR, exclude=exclude)
    return packages

def install_requires() -> typing.List[str]:
    """
    Read contents of requirements.txt file and return its relevant lines.

    Only non-empty and non-comment lines are relevant.
    """

    reqs = []
    with open(os.path.join(_HERE, 'requirements.txt')) as f:
        reqs = [l for l in f.read().splitlines() if l and not l.strip().startswith('#')]
    return reqs

def setup():
    """ Run setuptools.setup() with correct arguments. """

    name = 'argunparse'
    description = 'argunparse is intended to perform approximate reverse of argparse'
    url = 'http://mbdev.pl/'
    download_url = 'https://github.com/mbdevpl/argunparse'
    author = 'Mateusz Bysiek'
    author_email = 'mb@mbdev.pl'
    license_str = 'Apache License 2.0'
    keywords = ['argparse', 'unparsing', 'pretty printing']
    package_dir = {'': _SRC_DIR}
    entry_points = {
        }
    test_suite = 'test'

    setuptools.setup(
        name=name, version=version, description=description, long_description=long_description(),
        url=url, download_url=download_url, author=author, author_email=author_email,
        maintainer=author, maintainer_email=author_email, license=license_str,
        classifiers=classifiers(), keywords=keywords, packages=packages(), package_dir=package_dir,
        install_requires=install_requires(), entry_points=entry_points, test_suite=test_suite
        )

if __name__ == '__main__':
    clean()
    setup()
