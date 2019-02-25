#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
import subprocess
from setuptools import setup
from setuptools import find_packages
from distutils import log
from distutils.cmd import Command


class DocumentationCommand(Command):
    """ A custom documentation command using epydoc. """

    description = 'build html documentation'
    user_options = []

    def initialize_options(self):
        """ Set default values for options. """
        pass

    def finalize_options(self):
        """ Post-process options. """
        pass

    def run(self):
        """ Run command """
        command = ['epydoc',
                   '-v',
                   'pyfilesync',
                   '--html',
                   '-o',
                   'pyfilesync_docs']
        self.announce(
            'Running commnad: %s'.format(str(command)),
            level=log.INFO)
        subprocess.check_call(command)


def read_description(module_name):
    """ Read description. """
    module_doc = __import__(module_name).__doc__.splitlines()
    result = ""
    for line in module_doc:
        if line:
            result = line
            break
    return result

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 4)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================

This version of PyFileSync requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have python {}.{} or newer, then try again:

    $ python3 -m pip install --upgrade pip setuptools
    $ pip3 install pyfilesync

""".format(*REQUIRED_PYTHON + CURRENT_PYTHON + REQUIRED_PYTHON))
    sys.exit(1)

version = __import__('pyfilesync').get_version()

data_files = []

setup(
    name='pyfilesync',
    version=version,
    license='GNU',
    author="Marcin Kruk, Bartosz Gertych, Rafał Kobel",
    author_email="Kruk.marcin@o2.pl, bartoszgertych94@gmail.com, rafalkobel@rafyco.pl",
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    description=read_description('pyfilesync'),
    long_description=open("README.rst", encoding="utf-8").read(),
    url="https://github.com/MarcepanK/pyfilesync",
    packages=find_packages(),
    include_package_data=True,
    package_dir={'pyfilesync': 'pyfilesync'},
    test_suite='pyfilesync.tests.__main__',
    classifiers=[
        'Environment :: Console',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Archiving :: Backup',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    install_requires=[
        'pylint==1.9.1',
        'pep8==1.7.1'
    ],
    cmdclass={
        'documentation': DocumentationCommand,
    },
    entry_points={
        'console_scripts': [
            'filesync = pyfilesync.console:main',
        ]
    },
    command_options={
        'build_sphinx': {
            'project': ('setup.py', 'pyFileSync'),
            'version': ('setup.py', 'version'),
            'release': ('setup.py', 'version'),
            'source_dir': ('setup.py', 'docs')
        }
    },
    platforms="Any",
    keywords="backup, synchronization, p2p, torrent"
)
