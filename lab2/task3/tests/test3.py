import unittest
import datetime
from time import perf_counter
from lab2.task3.src.task3 import count_inverse


class TestCountInversion(unittest.TestCase):
    print("Lab2 task3 test")
    def test_should_count_inversions1(self):
        # given
        list1 = [1, 3, 5, 2, 4, 6]
        n = len(list1)
        expect_result = 3
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = count_inverse(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_inversions2(self):
        # given
        list1 = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        n = len(list1)
        expect_result = 17
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = count_inverse(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_count_inversions_when_array_is_reversed(self):
        # Given
        list1 = [i for i in range(1000,0,-1)]
        n = len(list1)

        # given
        list1 = [i for i in range(1000,0,-1)]
        n = len(list1)
        expect_result = 499500
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = count_inverse(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == '__main__':
    unittest.main()