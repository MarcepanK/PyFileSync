#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CommandLine interface for test.

For checking tests call::

    python -m wawsync.tests
"""

# pylint: disable=W0611
from __future__ import unicode_literals
import unittest
from wawsync.tests import TestWawSyncModule


if __name__ == "__main__":
    unittest.main()
