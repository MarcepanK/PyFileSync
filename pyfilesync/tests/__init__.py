#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
import os
import pep8
from pylint.lint import Run
import pyfilesync


# This is tested class. Can have too many method
class TestPyFileSyncModule(unittest.TestCase):  # pylint: disable=R0904
    """ Module testsCase. """
    @staticmethod
    def __get_sources_file():
        """ Get all paths to source files in pyfilesync module. """

        def recursive_checker(main_directory):
            """ Recursive function to find all source file in direcotry. """
            result = []
            for source_file in os.listdir(main_directory):
                if (source_file.endswith(".py") and
                        os.path.isfile(os.path.join(main_directory,
                                                    source_file))):
                    result.append(os.path.join(main_directory, source_file))
                elif os.path.isdir(os.path.join(main_directory, source_file)):
                    result = (result +
                              recursive_checker(os.path.join(main_directory,
                                                             source_file)))
            return result
        return recursive_checker(pyfilesync.__path__[0])

    def test_pap8(self):
        """ Test that we conform to PEP8. """
        pep8_style = pep8.StyleGuide(paths=['--ignore=E501'])
        # Disable E501 code (line too long). It should be enabled after fixed.
        result = pep8_style.check_files(pyfilesync.__path__)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pylint(self):
        """ Documentation tests. """
        status = 0
        try:
            Run(['-d', 'I0011,R0801,R0902,R0903,R0921', 'pyfilesync'])
        except SystemExit as ex:
            status = int(ex.code)
        self.assertEqual(status, 0, "[Pylint] Found code style errors"
                                    " (and warnings).")


if __name__ == "__main__":
    unittest.main()
