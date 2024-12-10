import unittest
import random
import datetime
from time import perf_counter
from lab6.task1.src.task1 import process_operations

class TestProcesOperation(unittest.TestCase):

    def test_should_print_operation_result(self):
        # given
        n = 8
        list1 = [['A', '2'], ['A', '5'], ['A', '3'], ['?', '2'], ['?', '4'], ['A', '2'], ['D', '2'], ['?', '2']]
        expect_result = ['Y', 'N', 'N']
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_operations(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_empty_result(self):
        # given
        n = 0
        list1 = []
        expect_result = []
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_operations(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_result_of_adding_same_element(self):
        # given
        n = 5
        list1 = [['A', '10'], ['?', '10'], ['D', '10'], ['?', '10'], ['D', '10']]
        expect_result = ['Y', 'N']
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = process_operations(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()