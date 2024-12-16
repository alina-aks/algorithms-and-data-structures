import unittest
import random
import datetime
from time import perf_counter
from lab7.task1.src.task1 import min_coins

class TestMinCoins(unittest.TestCase):
    def test_should_print_min_coins(self):
        # given
        n = 2
        list1 = [1, 3, 4]
        expect_result = 2
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = min_coins(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_min_coins2(self):
        # given
        n = 34
        list1 = [1, 3, 4]
        expect_result = 9
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = min_coins(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()