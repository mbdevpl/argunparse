"""Setup script for argunparse package."""

import setup_boilerplate


class Package(setup_boilerplate.Package):
    """Package metadata."""

    name = 'argunparse'
    description = 'Reversed argparse: generate string of command-line args from Python objects.'
    url = 'https://github.com/mbdevpl/argunparse'
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
        ]
    keywords = ['argparse', 'commandline arguments', 'pretty printing', 'unparsing']


if __name__ == '__main__':
    Package.setup()
