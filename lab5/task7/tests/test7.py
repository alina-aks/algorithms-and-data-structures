import unittest
import random
import datetime
from time import perf_counter
from lab5.task7.src.task7 import heap_sort

task_numb = 7

class TestHeap(unittest.TestCase):
    print(f"Lab5 task{task_numb} test")
    def test_should_sort_small_list(self):
        # given
        n = 5
        list1 = [3, 4, 5, 2, 1]
        expect_result = [1, 2, 3, 4, 5]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = heap_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list(self):
        # given
        n = 1000
        list1 = [random.randint(1, 10**9) for _ in range(n)]
        expect_result = sorted(list1)
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = heap_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list2(self):
        # given
        n = 10000
        list1 = [random.randint(1, 10**9) for _ in range(n)]
        expect_result = sorted(list1)
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = heap_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list3(self):
        # given
        n = 100000
        list1 = [random.randint(1, 10**9) for _ in range(n)]
        list1.sort(reverse=True)
        expect_result = heap_sort(list1)
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = heap_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_sorted_list(self):
        # given
        n = 100000
        list1 = [random.randint(1, 10**9) for _ in range(n)]
        list1.sort()
        expect_result = heap_sort(list1)
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = heap_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест5.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_repeated_list(self):
        # given
        n = 10
        list1 = [10, 4, 5, 7, 7, 4, 10, 5, 4, 3]
        expect_result = [3, 4, 4, 4, 5, 5, 7, 7, 10, 10]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = heap_sort(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест6.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()