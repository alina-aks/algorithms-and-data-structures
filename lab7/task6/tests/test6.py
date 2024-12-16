import unittest
import random
import datetime
from time import perf_counter
from lab7.task6.src.task6 import increasing_sequence

class TestIncreasingSequence(unittest.TestCase):
    def test_should_print_sequence(self):
        # given
        n = 6
        list1 = [3, 29, 5, 5, 28, 6]
        expect_result = (3, [3, 5, 28])
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = increasing_sequence(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_sequence2(self):
        # given
        n = 6
        list1 = [3, 29, 5, 5, 28, 6]
        expect_result = (3, [3, 5, 28])
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = increasing_sequence(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_large_sequence(self):
        # given
        n = 1000
        list1 = list(range(1, 1001))
        expect_result = (1000, list1)
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = increasing_sequence(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()