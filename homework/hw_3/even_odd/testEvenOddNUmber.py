import unittest
from evenOddNumber import EvenOddNumber


class Test_EvenOddNumber(unittest.TestCase):

    def test_evenOddNumber_even(self):
        self.assertTrue(EvenOddNumber(0))
        self.assertTrue(EvenOddNumber(4))
        self.assertTrue(EvenOddNumber(6))

    def test_EvenOddNumber_odd(self):
        self.assertFalse(EvenOddNumber(7))
        self.assertFalse(EvenOddNumber(9))
        self.assertFalse(EvenOddNumber(13))

    def test_type_number(self):
        with self.assertRaises(TypeError):
            EvenOddNumber("number")
