import unittest
import random
import datetime
from time import perf_counter
from lab3.task4.src.task4 import lottery

class TestSegmentsCount(unittest.TestCase):
    print("Lab3 task4 test")
    def test_should_count_segments1(self):
        # given
        s = 2
        p = 3
        seg = [[0, 5], [7, 10]]
        pont = [1, 6, 11]

        expect_result = [1, 0, 0]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = lottery(s,p,seg,pont)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_segments2(self):
        # given
        s = 1
        p = 3
        seg = [[-10, 10]]
        pont = [-100, 100, 0]

        expect_result = [0, 0, 1]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = lottery(s,p,seg,pont)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_segments3(self):
        # given
        s = 3
        p = 2
        seg = [[0, 5],[-3, 2],[7, 10]]
        pont = [1, 6]

        expect_result = [2, 0]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = lottery(s,p,seg,pont)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()