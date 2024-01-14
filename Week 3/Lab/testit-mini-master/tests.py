"""
CIS 211

Ernest Ho

Credits:

Unit tests for testme.py
"""
#File: tests.py

import unittest
from buggy import *


class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_1(self):
        """Doesn't count the last numbers as the longest running
        The error here is that it counts [5,5] as the longest running
        instead of [1,1,1,1] because it needs an extra statement
        in order for it to work."""
        self.assertEqual(max_run([1, 2, 5, 5, 1, 1, 1, 1]), [1, 1, 1, 1])

    """"
    def test_max_run_2(self):
        self.assertEqual(max_run([1, 1, 1, 1, 3, 6, 9]), [1, 1, 1, 1])
        # no bugs here
    """

    """
    def test_max_run_3(self):
        self.assertEqual(max_run([1, 1, 1, 2, 2, 3]), [1, 1, 1])
        # no bugs here
    """

    def test_max_run_4(self):
        """Error here is that it can't calculate and empty list
        cause it's out of range."""
        self.assertEqual(max_run([]), 0)


if __name__ == "__main__":
    unittest.main()
