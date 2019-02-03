#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Package allows you backup files between your host and remote directory.

Insallation
===========

There are a two metod of installation C{wawsync} module.

From PyPI repository (not implemented yet)::

    pip3 install wawsync

From sources::

    git clone git@bitbucket.org:MarepanK/WawSync.git
    cd wawsync
    python3 setup.py install

Usage
=====

    wawsync --help

"""

from __future__ import unicode_literals


def get_version():
    """ Get version of wawsync package. """
    return "0.0.1"

__version__ = get_version()
