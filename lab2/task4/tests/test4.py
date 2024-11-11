import unittest
import datetime
from time import perf_counter
from lab2.task4.src.task4 import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_should_return_index_when_element_is_found(self):
        # Given
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 5

        # When
        start_time = datetime.datetime.now()
        binary_search(list1, n)
        finish_time = datetime.datetime.now()
        print("Тест1.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(binary_search(list1, n), 4)

    def test_should_return_negative_one_when_element_is_not_found(self):
        # Given
        list1 = [1, 2, 3, 4, 5]
        n = 6

        # When
        start_time = datetime.datetime.now()
        binary_search(list1, n)
        finish_time = datetime.datetime.now()
        print("Тест2.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(binary_search(list1, n), -1)


if __name__ == '__main__':
    unittest.main()