import unittest
import random
import datetime
from time import perf_counter
from lab3.task6.src.task6 import sorting_integers

class TestIndexHarsh(unittest.TestCase):
    def test_should_count_sum_of_tenths_example(self):
        # given
        listA = [7, 1, 4, 9]
        listB = [2, 7, 8, 11]
        expect_result = 51
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = sorting_integers(listA, listB)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_sum_of_tenths_for_bigger_lists(self):
        # given
        listA = [1, 3, 5, 7, 9]
        listB = [2, 4, 6, 8, 10, 12]
        expect_result = 62
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = sorting_integers(listA, listB)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_sum_of_tenths_for_empty_lists(self):
        # given
        listA = []
        listB = []
        expect_result = 0
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = sorting_integers(listA, listB)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()