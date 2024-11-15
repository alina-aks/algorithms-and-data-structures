# Задание №4 по выбору : `Бинарный поиск`
Студентка ИТМО, Аксянова Алина Рустамовна  464950

## Вариант 1

## Задание 
В этой задаче вы реализуете алгоритм бинарного поиска, который позволяет очень эффективно искать (даже в огромных) списках при условии, что список отсортирован. Цель - реализация алгоритма дво-ичного (бинарного) поиска. 
Формат входного файла (input.txt). В первой строке входного файла со- держится число n (1 ≤ n ≤ 105) — число элементов в мас-сиве, и последо- вательность a0 < a1 < ... < an−1 из n различных положительных целых чисел в порядке возрастания, 1 ≤ ai ≤ 109 для всех 0 ≤ i < n. Следующая строка содержит число k, 1 ≤ k ≤ 105 и k положительных целых чисел b0,...bk−1,1≤bj ≤109 длявсех0≤j <k. 
Формат выходного файла (output.txt). Для всех i от 0 до k − 1 вывести индекс0≤j ≤n−1,такойчтоai =bj или-1,еслитакогочиславмассиве нет. 


## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/alina-aks/algorithms-and-data-structures.git
   
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algorithms-and-data-structures/lab2
   ```
3. Запустите программу:
   ```bash
   python src/task4.py
   ```

4. Запуск тестов:
   ```bash
   python src/tesk4.py
   ```