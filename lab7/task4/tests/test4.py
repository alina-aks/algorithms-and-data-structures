import unittest
import random
import datetime
from time import perf_counter
from lab7.task4.src.task4 import longest_common_subsequence

class TestSubsequence(unittest.TestCase):
    def test_should_print_length_subsequence(self):
        # given
        n = 3
        list1 = [2, 7, 5]
        m = 2
        list2 = [2, 5]
        expect_result = 2
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = longest_common_subsequence(n, list1, m, list2)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_length_subsequence2(self):
        # given
        n = 1
        list1 = [7]
        m = 4
        list2 = [1, 2, 3, 4]
        expect_result = 0
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = longest_common_subsequence(n, list1, m, list2)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_length_subsequence3(self):
        # given
        n = 4
        list1 = [2, 7, 8, 3]
        m = 4
        list2 = [5, 2, 8, 7]
        expect_result = 2
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = longest_common_subsequence(n, list1, m, list2)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()