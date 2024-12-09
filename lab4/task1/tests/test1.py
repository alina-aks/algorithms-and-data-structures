import unittest
import random
import datetime
from time import perf_counter
from lab4.task1.src.task1 import process_stack_commands

class TestStack(unittest.TestCase):
    def test_should_print_deleted_numbs(self):
        # given
        c = ["+ 1", "+ 10", "-" ,"+ 2", "+ 1234", "-"]
        expect_result = [10, 1234]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_stack_commands(c)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_deleted_numbs2(self):
        # given
        c = ["+ 1", "+ 2", "+ 3", "+ 4", "+ 5", "-", "-", "-", "-", "-"]
        expect_result = [5, 4, 3, 2, 1]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_stack_commands(c)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_empty_list(self):
        # given
        c = ["+ 100", "+ 200", "+ 300"]
        expect_result = []
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_stack_commands(c)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()