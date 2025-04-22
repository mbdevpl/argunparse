"""Setup script for argunparse package."""

import boilerplates.setup


class Package(boilerplates.setup.Package):
    """Package metadata."""

    name = 'argunparse'
    description = 'Reversed argparse: generate string of command-line args from Python objects.'
    url = 'https://github.com/mbdevpl/argunparse'
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',
        'Typing :: Typed']
    keywords = ['argparse', 'commandline arguments', 'pretty printing', 'unparsing']


if __name__ == '__main__':
    Package.setup()
