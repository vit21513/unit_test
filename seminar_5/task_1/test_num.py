import unittest
from random_gen import random_list
from max_gen import max_mum


class test_rand(unittest.TestCase):

    def test_rnd(self):
        temp = random_list()
        result = max_mum(temp)
        maxim = sorted(temp)[-1]
        self.assertEqual(result,maxim)


