import unittest
import random
import datetime
from time import perf_counter
from lab7.task5.src.task5 import subsequence

class TestSubsequence(unittest.TestCase):
    def test_should_print_length_subsequence(self):
        # given
        n = 3
        list1 = [1, 2, 3]
        m = 3
        list2 = [2, 1, 3]
        l = 3
        list3 = [1, 3, 5]
        expect_result = 2
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = subsequence(n, list1, m, list2, l, list3)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_length_subsequence2(self):
        # given
        n = 5
        list1 = [8, 3, 2, 1, 7]
        m = 7
        list2 = [8, 2, 1, 3, 8, 10, 7]
        l = 6
        list3 = [6, 8, 3, 1, 4, 7]
        expect_result = 3
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = subsequence(n, list1, m, list2, l, list3)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")



if __name__ == "__main__":
    unittest.main()