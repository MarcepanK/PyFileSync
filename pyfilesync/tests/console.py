#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testing module console.
"""

from __future__ import unicode_literals
import unittest
import sys
from io import StringIO
import pyfilesync
from pyfilesync.console import main


# This is tested class. Can have too many method
class TestConsoleModule(unittest.TestCase):  # pylint: disable=R0904
    """ Module testsCase. """

    def setUp(self):
        """ Setup environment. """
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        sys.stdout = self.tmp_stdout = StringIO()
        sys.stderr = StringIO()

    def tearDown(self):
        """ Teardown environment. """
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

    def test_console(self):
        """ Test that console app work ok. """
        status = 0
        try:
            main(["--help"])
        except SystemExit as ex:
            if ex.code is not None:
                status = ex.code  # pylint disable=E0012,R0204
        self.assertEqual(status, 0)
        self.assertNotEqual(self.tmp_stdout.getvalue(), "")

    def test_invalid_args(self):
        """ Test invalid arguments. """
        status = 0
        try:
            main(["--invalid-arg", "--another-invalid-arg"])
        except SystemExit as ex:
            if ex.code is not None:
                status = ex.code  # pylint disable=E0012,R0204
        self.assertEqual(self.tmp_stdout.getvalue(), "")
        self.assertNotEqual(status, 0)

    def test_version(self):
        """ Test invalid arguments. """
        status = 0
        try:
            main(["--version"])
        except SystemExit as ex:
            if ex.code is not None:
                status = ex.code  # pylint disable=E0012,R0204
        self.assertEqual(status, 0)
        self.assertEqual(self.tmp_stdout.getvalue().strip(),
                         "filesync {}".format(pyfilesync.get_version()))

if __name__ == "__main__":
    unittest.main()
