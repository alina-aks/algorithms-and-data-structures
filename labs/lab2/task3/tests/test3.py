import unittest
from labs.lab2.task3.src.task3 import count_inverse


class TestCountInversion(unittest.TestCase):
    def test_3(self):
        self.assertEqual(count_inverse(6,[1, 3, 5, 2, 4, 6]), 3)
        self.assertEqual(count_inverse(10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]), 17)
        sp = [i for i in range(1000,0,-1)]
        self.assertEqual(count_inverse(len(sp), sp), 499500)