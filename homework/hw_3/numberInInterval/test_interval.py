import unittest
from num_interval import interval


class Test_EvenOddNumber(unittest.TestCase):

    def test_interval_false(self):
        self.assertFalse(interval(5))
        self.assertFalse(interval(500))
        self.assertFalse(interval(-5))

    def test_interval_true(self):
        self.assertTrue(interval(25))
        self.assertTrue(interval(100))
        self.assertTrue(interval(46))

    def test_interval_incorrect_args(self):
        with self.assertRaises(AssertionError):
            interval("number")
        with self.assertRaises(AssertionError):
            interval(5.33)
        with self.assertRaises(AssertionError):
            interval(True)
