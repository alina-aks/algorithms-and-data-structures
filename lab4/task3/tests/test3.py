import unittest
import random
import datetime
from time import perf_counter
from lab4.task3.src.task3 import is_valid_sequence

class TestStack(unittest.TestCase):
    print("Lab4 task3 test")
    def test_should_check_sequence1(self):
        # given
        s1 = "()()"
        s2 = "([])"
        s3 = "([)]"
        s4 = "((]]"
        s5 = ")("
        expect_result1 = "YES"
        expect_result2 = "YES"
        expect_result3 = "NO"
        expect_result4 = "NO"
        expect_result5 = "NO"
        expected_time = 2

        #when
        start_time = datetime.datetime.now()
        result1 = is_valid_sequence(s1)
        result2 = is_valid_sequence(s2)
        result3 = is_valid_sequence(s3)
        result4 = is_valid_sequence(s4)
        result5 = is_valid_sequence(s5)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result1, expect_result1)
        self.assertEqual(result2, expect_result2)
        self.assertEqual(result3, expect_result3)
        self.assertEqual(result4, expect_result4)
        self.assertEqual(result5, expect_result5)
        self.assertLessEqual(result_time.total_seconds(), expected_time,f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_valid_sequences(self):
        # given
        s1 = "()"
        s2 = "()[]"
        s3 = "(())"
        s4 = "([])"
        s5 = "([([])])"
        expect_result1 = "YES"
        expect_result2 = "YES"
        expect_result3 = "YES"
        expect_result4 = "YES"
        expect_result5 = "YES"
        expected_time = 2

        #when
        start_time = datetime.datetime.now()
        result1 = is_valid_sequence(s1)
        result2 = is_valid_sequence(s2)
        result3 = is_valid_sequence(s3)
        result4 = is_valid_sequence(s4)
        result5 = is_valid_sequence(s5)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result1, expect_result1)
        self.assertEqual(result2, expect_result2)
        self.assertEqual(result3, expect_result3)
        self.assertEqual(result4, expect_result4)
        self.assertEqual(result5, expect_result5)
        self.assertLessEqual(result_time.total_seconds(), expected_time,f"Значение {result_time} превышает порог {expected_time}")

    def test_should_check_invalid_sequences(self):
        # given
        s1 = "()[]]]"
        s2 = "(]"
        s3 = "(()]]])"
        s4 = "(])"
        s5 = "([([]]]]"
        expect_result1 = "NO"
        expect_result2 = "NO"
        expect_result3 = "NO"
        expect_result4 = "NO"
        expect_result5 = "NO"
        expected_time = 2

        #when
        start_time = datetime.datetime.now()
        result1 = is_valid_sequence(s1)
        result2 = is_valid_sequence(s2)
        result3 = is_valid_sequence(s3)
        result4 = is_valid_sequence(s4)
        result5 = is_valid_sequence(s5)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result1, expect_result1)
        self.assertEqual(result2, expect_result2)
        self.assertEqual(result3, expect_result3)
        self.assertEqual(result4, expect_result4)
        self.assertEqual(result5, expect_result5)
        self.assertLessEqual(result_time.total_seconds(), expected_time,f"Значение {result_time} превышает порог {expected_time}")



if __name__ == "__main__":
    unittest.main()

