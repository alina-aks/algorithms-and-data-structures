# Задание №7 по варианту  : `Максимум в движущейся последовательности`
Студентка ИТМО, Аксянова Алина Рустамовна  464950

## Вариант 1

## Задание 
Задан массив из n целых чисел - a1,...,an и число m < n, нужно найти максимум среди последовательности ("окна") {ai,...,ai+m−1} для каждого значения 1 ≤ i ≤ n − m +1. Простой алгоритм решения этой задачи за O(nm) сканирует каждое "окно"отдельно.
Ваша цель - алгоритм за O(n).
• Формат входного файла (input.txt). В первой строке содержится целое числоn(1 ≤ n ≤ 105)–количествочиселвисходноммассиве,втораястрока содержит n целых чисел a1,...,an этого массива, разделенных пробелом
(0 ≤ ai ≤ 105). В третьей строке - целое число m - ширина "окна"(1 ≤ m ≤ n).
•	Формат выходного файла (output.txt). Нужно вывести maxai,...,ai+m−1 для каждого 1 ≤ i ≤ n − m +1.


## Ограничения по времени и памяти

- Ограничение по времени. 5сек.
- Ограничение по памяти. 512 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/alina-aks/algorithms-and-data-structures.git
   
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algorithms-and-data-structures/lab4
   ```
3. Запустите программу:
   ```bash
   python src/task7.py
   ```

4. Запуск тестов:
   ```bash
   python src/test7.py
   ```
