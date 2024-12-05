import unittest
import random
import datetime
from time import perf_counter
from lab5.task1.src.task1 import Pyramid
from lab5.task4.src.task4 import build_heap

task_numb = 4

class TestHeap(unittest.TestCase):
    print(f"Lab5 task{task_numb} test")
    def test_should_count_swaps(self):
        # given
        n = 5
        list1 = [5, 4, 3, 2, 1]
        expect_result = [(1, 4), (0, 1), (1, 3)]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = build_heap(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_swaps2(self):
        # given
        n = 5
        list1 = [1, 2, 3, 4, 5]
        expect_result = []
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = build_heap(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_swaps_empty(self):
        # given
        n = 1
        list1 = [10]
        expect_result = []
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = build_heap(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_no_swaps(self):
        # given
        n = 5
        list1 = [1, 2, 3, 4, 5]
        expect_result = []
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = build_heap(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()