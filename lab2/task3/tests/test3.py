import unittest
import datetime
from lab2.task3.src.task3 import count_inverse


class TestCountInversion(unittest.TestCase):
    def test_should_count_inversions1(self):
        # Given
        n = 6
        list1 = [1, 3, 5, 2, 4, 6]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        count_inverse(n, list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест1.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(count_inverse(n, list1), 3)

    def test_should_count_inversions2(self):
        # Given
        n = 10
        list1 = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        count_inverse(n, list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест2.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(count_inverse(n, list1), 17)

    def test_should_count_inversions_when_array_is_reversed(self):
        # Given
        list1 = [i for i in range(1000,0,-1)]
        n = len(list1)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        count_inverse(n, list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест3.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(count_inverse(len(list1), list1), 499500)