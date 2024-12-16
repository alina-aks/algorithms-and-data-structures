import unittest
import random
import datetime
from time import perf_counter
from lab6.task2.src.task2 import Phonebook

class TestProcesOperation(unittest.TestCase):

    def test_should_print_result_of_operation(self):
        # given
        n = 8
        list1 = [['add', '911', 'police'], ['add', '76213', 'Mom'], ['add', '17239', 'Bob'], ['find', '76213'], ['find', '910'], ['find', '911'], ['del', '910'], ['del', '911'], ['find', '911'], ['find', '76213'], ['add', '76213', 'daddy'], ['find', '76213']]
        expect_result = ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy']
        expected_time = 6

        # when
        start_time = datetime.datetime.now()
        result = Phonebook(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_result_of_repeated_operations(self):
        # given
        n = 4
        list1 = [['add', '911', 'police'], ['add', '911', 'hospital'], ['find', '911'], ['find', '911']]
        expect_result = ['hospital', 'hospital']
        expected_time = 6

        # when
        start_time = datetime.datetime.now()
        result = Phonebook(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_result_of_deleting_operations(self):
        # given
        n = 4
        list1 = [['add', '911', 'police'], ['del', '911'], ['find', '911'], ['del', '911']]
        expect_result = ['not found']
        expected_time = 6

        # when
        start_time = datetime.datetime.now()
        result = Phonebook(n, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()