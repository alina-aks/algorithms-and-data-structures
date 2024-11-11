import unittest
import datetime
from time import perf_counter
from lab2.task5.src.task5 import chek_max_el

class TestFindMax(unittest.TestCase):
    def test_should_give_zero(self):
        # Given
        list1 = [1, 2, 3, 4]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        chek_max_el(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест1.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(chek_max_el(list1), 0)

    def test1_should_give_one(self):
        # Given
        list1 = [2, 3, 9, 2, 2]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        chek_max_el(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест2.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(chek_max_el(list1), 1)

    def test2_should_give_one(self):
        # Given
        list1 = [3, 6, 1, 3 ,6 ,3, 3, 3]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        chek_max_el(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест3.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(chek_max_el(list1), 1)