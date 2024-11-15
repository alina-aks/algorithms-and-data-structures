import unittest
import datetime
from time import perf_counter
from lab2.task5.src.task5 import chek_max_el

class TestFindMax(unittest.TestCase):

    def test_should_give_zero(self):
        # given
        list1 = [1, 2, 3, 4]
        expect_result = 0
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = chek_max_el(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test1_should_give_one(self):
        # Given
        list1 = [2, 3, 9, 2, 2]

        # given
        list1 = [2, 3, 9, 2, 2]
        expect_result = 1
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = chek_max_el(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_give_one(self):
        # Given
        list1 = [3, 6, 1, 3 ,6 ,3, 3, 3]

        # given
        list1 = [3, 6, 1, 3 ,6 ,3, 3, 3]
        expect_result = 1
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = chek_max_el(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")