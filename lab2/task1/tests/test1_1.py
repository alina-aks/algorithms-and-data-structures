import unittest
import random
import datetime
from time import perf_counter
from lab2.task1.src.task1_1 import merge_sort

# class TestMergeSort(unittest.TestCase):
#     def test_test1_1(self):
#         self.assertEqual(merge_sort([1, 2, 3, 4, 5]),[1, 2, 3, 4, 5]) #отсортированный список
#         self.assertEqual(merge_sort([24, 44, 3, 23, 1]), [1, 3, 23, 24, 44]) #рандом
#         pr = random.sample(range(-10**9, 10**9), 1000)
#         self.assertEqual(merge_sort(pr), sorted(pr))
#         pr2 = list(range(1,100001))
#         self.assertEqual(merge_sort(pr2), pr2)
#
# if __name__ == '__main__':
#     unittest.main()

class TestMergeSort(unittest.TestCase):
    def test_should_sort_sorted_list(self):
        # Given
        list1 = [1, 2, 3, 4, 5]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        merge_sort(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест1.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(merge_sort(list1), sorted(list1))

    def test_should_sort_list(self):
        # Given
        list1 = [24, 44, 3, 23, 1]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        merge_sort(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест2.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(merge_sort(list1), sorted(list1))

    def test_should_sort_large_list(self):
        # Given
        large_size = 10 ** 5
        list1 = [random.randint(-10 ** 9, 10 ** 9) for _ in range(large_size)]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        merge_sort(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест3.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(merge_sort(list1), sorted(list1))

    def test_should_sort_large_sorted_list(self):
        # Given
        list1 = list(range(1,100001))

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        merge_sort(list1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        print("Тест4.Итоговое время алгоритма:", finish_time - start_time)

        # Then
        self.assertEqual(merge_sort(list1), sorted(list1))


if __name__ == "__main__":
    unittest.main()