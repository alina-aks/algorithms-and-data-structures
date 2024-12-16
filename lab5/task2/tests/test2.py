import unittest
import random
import datetime
from time import perf_counter
from lab5.task2.src.task2 import tree_height

class TestPyramid(unittest.TestCase):
    def test_should_count_tree_height(self):
        # given
        n = 5
        list1 = [4, -1, 4, 1, 1]
        expect_result = 3
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = tree_height(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_tree_height2(self):
        # given
        n = 5
        list1 = [-1, 0, 4, 0, 3]
        expect_result = 4
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = tree_height(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_binary_tree_height(self):
        # given
        n = 7
        list1 = [-1, 0, 0, 1, 1, 2, 2]
        expect_result = 3
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = tree_height(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_max_tree_height(self):
        # given
        n = 100000
        list1 = [-1]
        for i in range(1, n):
            list0 = random.randint(0, i - 1)
            list1.append(list0)
        expect_result = tree_height(n, list1)
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = tree_height(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_deep_tree_height(self):
        # given
        n = 10
        list1 = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        expect_result = 10
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = tree_height(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест5.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()