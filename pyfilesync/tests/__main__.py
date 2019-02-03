#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CommandLine interface for test.

For checking tests call::

    python -m pyfilesync.tests
"""

# pylint: disable=W0611
from __future__ import unicode_literals
import unittest
from pyfilesync.tests import TestPyFileSyncModule


if __name__ == "__main__":
    unittest.main()
