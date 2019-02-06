#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Package allows you to backup files between your host and remote directory.

Installation
+===========

There are a two methods of Installation C{pyfilesync} module.

From PyPI repository (not implemented yet)::

    pip3 install pyfilesync

From sources::

    git clone git@github.com:MarepanK/pyfilesync.git
    cd pyfilesync
    python3 setup.py install

Usage
=====

    filesync --help

"""

from __future__ import unicode_literals


def get_version():
    """ Get version of pyfilesync package. """
    return "0.0.1"

__version__ = get_version()
