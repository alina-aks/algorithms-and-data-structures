import unittest
import random
import datetime
from time import perf_counter
from lab4.task8.src.task8 import postfix
task_numb = 8

class TestStack(unittest.TestCase):
    print(f"Lab4 task{task_numb} test")
    def test_should_print_postfix_result(self):
        # given
        n = 7
        list1 = "8 9 + 1 7 - *"
        expect_result = -102
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = postfix(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_numb_postfix_result(self):
        # given
        n = 1
        list1 = '42'
        expect_result = 42
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = postfix(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_large_postfix_result(self):
        # given
        n = 9
        list1 =  "1 2 3 * + 4 5 * +"
        expect_result = 27
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = postfix(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()