import unittest
import random
import datetime
from time import perf_counter
from lab4.task7.src.task7 import moving_equence_maximum

class TestStack(unittest.TestCase):
    print("Lab4 task7 test")
    def test_should_print_max_subsequence_of_moving_equence(self):
        # given
        n = 8
        m = 4
        list1 = [2, 7, 3, 1, 5, 2, 6, 2]
        expect_result = [7, 7, 5, 6, 6]
        expected_time = 5

        # when
        start_time = datetime.datetime.now()
        result = moving_equence_maximum(n, list1, m)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_max_elem_of_moving_equence(self):
        # given
        n = 6
        m = 6
        list1 = [6, 2, 4, 1, 9, 8]
        expect_result = [9]
        expected_time = 5

        # when
        start_time = datetime.datetime.now()
        result = moving_equence_maximum(n, list1, m)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_max_subsequence_of_large_moving_equence(self):
        # given
        n = 100000
        m =10
        list1 = list(range(n))
        expect_result = list(range(9, n))
        expected_time = 5

        # when
        start_time = datetime.datetime.now()
        result = moving_equence_maximum(n, list1, m)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()