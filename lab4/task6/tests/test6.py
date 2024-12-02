import unittest
import random
import datetime
from time import perf_counter
from lab4.task6.src.task6 import process_commands

class TestStack(unittest.TestCase):
    print("Lab4 task6 test")
    def test_should_print_min_elem_of_queue1(self):
        # given
        list1 = ['+1', '?', '+ 10', '?', '-', '?', '-']
        expect_result = ["1", "1", "10"]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_commands(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_min_elem_of_queue2(self):
        # given
        list1 = ["+ 145","?", "+ 19", "+ 14", "- 4",  "-", "?", "+33"]
        expect_result = ["145", "14"]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_commands(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_min_elem_of_queue3(self):
        # given
        list1 = ["+1000000000", "+999999999", "?", "-", "?"]
        expect_result = ["999999999", "999999999"]
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_commands(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == "__main__":
    unittest.main()