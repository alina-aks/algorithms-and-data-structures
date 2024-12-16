import unittest
import datetime
from lab6.task8.src.task8 import hash_table

class TestHashTable(unittest.TestCase):

    def test_should_print_hash(self):
        # given
        n, x, a, b, A_c, B_c, A_d, B_d = 4, 0, 0, 0, 1, 1, 0, 0
        expect_result = (3, 1, 1)
        expected_time = 5

        # when
        start_time = datetime.datetime.now()
        result = hash_table(n, x, a, b, A_c, B_c, A_d, B_d)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_hash_min_values(self):
        # given
        n, x, a, b, A_c, B_c, A_d, B_d = 1, 0, 0, 0, 0, 0, 0, 0
        expect_result = (0, 0, 0)
        expected_time = 5

        # when
        start_time = datetime.datetime.now()
        result = hash_table(n, x, a, b, A_c, B_c, A_d, B_d)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_hash_large_(self):
        # given
        n, x, a, b, A_c, B_c, A_d, B_d = 3, 999999999999999, 999, 999999999999999, 500, 1000000000000, 300, 500000000000
        expect_result = (261499999844434, 45, 1499999999999)
        expected_time = 5

        # when
        start_time = datetime.datetime.now()
        result = hash_table(n, x, a, b, A_c, B_c, A_d, B_d)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()