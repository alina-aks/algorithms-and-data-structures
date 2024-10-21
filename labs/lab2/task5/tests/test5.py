import unittest
from labs.lab2.task5.src.task5 import chek_max_el

class TestFindMax(unittest.TestCase):
    def test5(self):
        self.assertEqual(chek_max_el([1, 2, 3, 4]),0)
        self.assertEqual(chek_max_el([2, 3, 9, 2, 2]), 1)
        self.assertEqual(chek_max_el([3, 6, 1, 3 ,6 ,4, 3, 3]), 1)