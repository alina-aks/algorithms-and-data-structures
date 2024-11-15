import unittest
import datetime
from time import perf_counter
from lab2.task4.src.task4 import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_should_return_index_when_element_is_found(self):
        # given
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 5
        expect_result = 4
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = binary_search(list1, n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_return_negative_one_when_element_is_not_found(self):
        # given
        list1 = [1, 2, 3, 4, 5]
        n = 6
        expect_result = -1
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = binary_search(list1, n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")
        # Then
        self.assertEqual(binary_search(list1, n), -1)


if __name__ == '__main__':
    unittest.main()