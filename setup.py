"""This is "setup.py" file for "argunparse"."""

import setup_boilerplate


class Package(setup_boilerplate.Package):

    """Package metadata."""

    name = 'argunparse'
    description = 'argunparse is intended to perform approximate reverse of argparse'
    download_url = 'https://github.com/mbdevpl/argunparse'
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
        ]
    keywords = ['argparse', 'commandline arguments', 'pretty printing', 'unparsing']


if __name__ == '__main__':
    Package.setup()
