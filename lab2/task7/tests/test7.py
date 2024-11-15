import unittest
import datetime
from time import perf_counter

from lab2.task5.src.task5 import find_max_elem
from lab2.task7.src.task7 import find_max_sum

class TestFindMax(unittest.TestCase):
    def test_should_give_max_list(self):
        # given
        list1 = [184, 343, -352, -4, 583,-248, 57, 34, 3, -5]
        expect_result = [184, 343, -352, -4, 583]
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = find_max_sum(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_give_the_same_sorted_list(self):
        # given
        list1 = [1, 2, 3, 4, 5]
        expect_result = list1
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = find_max_sum(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_give_empty_list(self):
        # given
        list1 = [-1, -2, -3, -4, -5]
        expect_result = []
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = find_max_sum(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_give_max_list_from_large_list(self):
        # given
        list1 = [10000, -146059, 496, -9483, 59384, 56, -49, 5749, -4]
        expect_result = [59384, 56, -49, 5749]
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = find_max_sum(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

