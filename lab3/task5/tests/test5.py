import unittest
import random
import datetime
from time import perf_counter
from lab3.task5.src.task5 import index_harsh

class TestIndexHarsh(unittest.TestCase):
    print("Lab3 task5 test")
    def test_should_find_h_index1(self):
        # given
        list1 = [3,0,6,1,5]
        expect_result = 3
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = index_harsh(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_find_h_index2(self):
        # given
        list1 = [1,3,1]
        expect_result = 1
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = index_harsh(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_find_h_index3(self):
        # given
        list1 = [10, 8, 5, 4, 3]
        expect_result = 4
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = index_harsh(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()