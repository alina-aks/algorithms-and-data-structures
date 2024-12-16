import unittest
import random
import datetime
from time import perf_counter
from lab5.task1.src.task1 import Pyramid

class TestPyramid(unittest.TestCase):
    def test_should_identify_pyramid(self):
        # given
        n = 5
        list1 = [1, 3, 2, 5, 4]
        expect_result = "YES"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = Pyramid(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_identify_pyramid2(self):
        # given
        n = 5
        list1 = [1, 0, 1, 2, 0]
        expect_result = "NO"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = Pyramid(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_identify_large_pyramid(self):
        # given
        n = 30
        list1 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10]
        expect_result = "YES"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = Pyramid(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_not_identify_large_pyramid(self):
        # given
        n = 30
        list1 = [5, 3, 4, 6, 1, 7, 2, 8, 5, 9, 6, 10, 3, 11, 4, 12, 7, 13, 8, 14, 9, 15, 10, 16, 11, 17, 12, 18, 13, 19]
        expect_result = "NO"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = Pyramid(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()