import unittest
import random
import datetime
from time import perf_counter
from lab3.task3.src.task3 import dolls

class TestDolls(unittest.TestCase):
    def test_should_sort_list1(self):
        # given
        n = 3
        k = 2
        list1 = [2, 1, 3]
        expect_result = "НЕТ"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = dolls(n, k, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_list2(self):
        # given
        n = 5
        k = 3
        list1 = [1, 5, 3, 4, 1]
        expect_result = "ДА"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = dolls(n, k, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


    def test_should_sort_large_sorted_list(self):
        # given
        n = 100_000
        k = 2
        list1 = list(range(1, n + 1))
        expect_result = "ДА"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = dolls(n, k, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


    def test_should_sort_large_random_list(self):
        # given
        n = 100_000
        k = 3
        list1 = random.sample(range(1, n + 1), n)
        expect_result = "НЕТ"
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = dolls(n, k, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()