#!/usr/bin/env python3
"""
Unit and regression test for the {{cookiecutter.repo_name}} package.
"""

# Import package, test suite, and other packages as needed
import os
import unittest
from common_wrangler.common import (capture_stdout, capture_stderr)
from {{cookiecutter.repo_name}}.{{cookiecutter.first_module_name}} import main

# Directories #

DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

class TestQuote(unittest.TestCase):
    def testNoArgs(self):
        test_input = []
        main(test_input)
        with capture_stdout(main, test_input) as output:
            self.assertTrue("Henry David Thoreau" in output)


    def testNoAttribution(self):
        test_input = ["-n"]
        main(test_input)
        with capture_stdout(main, test_input) as output:
            self.assertFalse("Henry David Thoreau" in output)

