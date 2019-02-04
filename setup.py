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

version = __import__('pyfilesync').get_version()

data_files = []

setup(
    name='pyfilesync',
    version=version,
    license='GNU',
    author="Marcin Kruk, Bartosz Gertych, Rafał Kobel",
    author_email="Kruk.marcin@o2.pl, bartoszgertych94@gmail.com, rafalkobel@rafyco.pl",
    description=read_description('pyfilesync'),
    long_description=open("README.rst").read(),
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
        'pylint',
        'pep8'
    ],
    cmdclass={
        'documentation': DocumentationCommand,
    },
    entry_points={
        'console_scripts': [
            'pyfilesync = pyfilesync.console:main',
        ]
    },
    platforms="Any",
    keywords="backup, synchronization, p2p, torrent"
)
