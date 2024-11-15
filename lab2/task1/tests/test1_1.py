import unittest
import random
import datetime
from time import perf_counter
from lab2.task1.src.task1_1 import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_should_sort_sorted_list(self):
        # given
        list1 = [1, 2, 3, 4, 5]
        expect_result = sorted(list1)
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = merge_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_list(self):
        # Given
        list1 = [24, 44, 3, 23, 1]
        expect_result = sorted(list1)
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = merge_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list(self):
        # given
        large_size = 10 ** 5
        list1 = [random.randint(-10 ** 9, 10 ** 9) for _ in range(large_size)]
        expect_result = sorted(list1)
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = merge_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_sorted_list(self):
        # given
        list1 = list(range(1,100001))
        expect_result = sorted(list1)
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = merge_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()