import unittest
import random
import datetime
from time import perf_counter
from lab3.task1.src.task1 import random_quick_sort

class TestQuickSort(unittest.TestCase):
    print("Lab3 task1 test")
    def test_should_sort_standart_list(self):
        # given
        list1 = [2, 3, 9, 2, 2]
        n = len(list1)
        expect_result = [2, 2, 2, 3, 9]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = random_quick_sort(list1, 0, n-1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_list_with_a_lot_of_identical_elements(self):
        # given
        list1 = [4, 7, 2, 6, 4, 5, 3, 7, 8, 5, 3, 6, 4, 7, 4, 5, 7, 4]
        n = len(list1)
        expect_result = [2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = random_quick_sort(list1, 0, n-1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list(self):
        # given
        list1 = [random.randint(-10**9, 10**9) for _ in range(10**4)]
        n = len(list1)
        expect_result = sorted(list1)
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = random_quick_sort(list1, 0, n-1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_list_with_all_identical_elements(self):
        # given
        list1 = [5] * 1000
        n = len(list1)
        expect_result = list1
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = random_quick_sort(list1, 0, n-1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()