import unittest
import datetime
from lab6.task7.src.task7 import Precious_stones

class TestPreciousStones(unittest.TestCase):

    def test_should_print_count_of_pairs(self):
        # given
        n, k = 7, 1
        s = "abacaba"
        list1 = ['aa']
        expect_result = 6
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = Precious_stones(n, k, s, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_count_of_pairs2(self):
        # given
        n, k = 7, 3
        s = "abacaba"
        list1 = ['ab', 'ac', 'bb']
        expect_result = 7
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = Precious_stones(n, k, s, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_no_pairs(self):
        # given
        n, k = 5, 0
        s = "abcab"
        list1 = []
        expect_result = 0
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = Precious_stones(n, k, s, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_test_all_pairs(self):
        # given
        n, k = 5, 2
        s = "abcab"
        list1 = [("a", "b"), ("b", "c")]
        expect_result = 2
        expected_time = 1

        # when
        start_time = datetime.datetime.now()
        result = Precious_stones(n, k, s, list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест4.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()