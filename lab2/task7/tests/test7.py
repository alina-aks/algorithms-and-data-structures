import unittest
import datetime
from time import perf_counter
from lab2.task7.src.task7 import find_max_sum

class TestFindMax(unittest.TestCase):
    def test_should_give_max_list(self):
        # Given
        list1 = [184, 343, -352, -4, 583,-248, 57, 34, 3, -5]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        find_max_sum(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест1.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(find_max_sum(list1), [184, 343, -352, -4, 583])

    def test_should_give_the_same_sorted_list(self):
        # Given
        list1 = [1, 2, 3, 4, 5]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        find_max_sum(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест2.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(find_max_sum(list1), list1)

    def test_should_give_empty_list(self):
        # Given
        list1 = [-1, -2, -3, -4, -5]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        find_max_sum(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест3.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(find_max_sum(list1), [])

    def test_should_give_max_list_from_large_list(self):
        # Given
        list1 = [10000, -146059, 496, -9483, 59384, 56, -49, 5749, -4]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        find_max_sum(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест4.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(find_max_sum(list1), [59384, 56, -49, 5749])

