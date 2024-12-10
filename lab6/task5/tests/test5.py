import unittest
import datetime
from lab6.task5.src.task5 import count_votes

class TestVoteCounter(unittest.TestCase):

    def test_should_print_count_of_votes(self):
        # given
        list1 = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
        expect_result = {'McCain': 16, 'Obama': 17}
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = count_votes(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_count_of_votes2(self):
        # given
        list1 = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
        expect_result = {'ivanov': 900, 'petr': 70, 'tourist': 3}
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = count_votes(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_print_count_of_votes3(self):
        # given
        list1 = ['bur 1']
        expect_result ={'bur': 1}
        expected_time = 2

        # when
        start_time = datetime.datetime.now()
        result = count_votes(list1)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == "__main__":
    unittest.main()