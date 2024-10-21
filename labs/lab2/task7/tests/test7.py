import unittest
from labs.lab2.task7.src.task7 import find_max_sum

class TestFindMax(unittest.TestCase):
    def test7(self):
        self.assertEqual(find_max_sum([184, 343, -352, -4, 583,-248, 57, 34, 3, -5]),[184, 343, -352, -4, 583])
        self.assertEqual(find_max_sum([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(find_max_sum([-1, -2, -3, -4, -5]),[ ] )
        self.assertEqual(find_max_sum([10000, -146059, 496, -9483, 59384, 56, -49, 5749, -4]), [59384, 56, -49, 5749])
