import unittest
import random
import datetime
from time import perf_counter
from lab3.task2.src.task2 import anti_quick_sort

class TestQuickSort(unittest.TestCase):
    print("Lab3 task2 test")
    def test_should_create_check_permutation_of_n_nums(self):
        # given
        n = 3
        expect_result = [1, 3, 2]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = anti_quick_sort(n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_create_check_permutation_of_n_nums2(self):
        # given
        n = 10
        expect_result = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = anti_quick_sort(n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_create_check_permutation_of_n_nums3(self):
        # given
        n = 30
        expect_result = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 15, 2, 17, 9, 19, 5, 21, 11, 23, 3, 25, 13, 27, 7, 29]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = anti_quick_sort(n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result, expect_result, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()