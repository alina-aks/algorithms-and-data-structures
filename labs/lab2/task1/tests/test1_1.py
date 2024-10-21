import unittest
import random
from labs.lab2.task1.src.task1_1 import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_test1_1(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]),[1, 2, 3, 4, 5]) #отсортированный список
        self.assertEqual(merge_sort([24, 44, 3, 23, 1]), [1, 3, 23, 24, 44]) #рандом
        pr = random.sample(range(-10**9, 10**9), 1000)
        self.assertEqual(merge_sort(pr), sorted(pr))
        pr2 = list(range(1,100001))
        self.assertEqual(merge_sort(pr2), pr2)