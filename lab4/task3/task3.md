# Задание №3 по варианту  : `Скобочная последовательность`
Студентка ИТМО, Аксянова Алина Рустамовна  464950

## Вариант 1

## Задание 
Последовательность A, состоящую из символов из множества «(», «)», «[» и
«]», назовем правильной скобочной последовательностью, если выполняется одно из следующих утверждений:
•	A – пустая последовательность;
•	первый символ последовательности A–это«(»,и в этойп оследовательности существует такой символ «)», что последовательность можно представить как A = (B)C, где B и C – правильные скобочные последовательности;
•	первый символ последовательности A–это«[»,и в этой последовательности существует такой символ «]», что последовательность можно представить как A = (B)C, где B и C – правильные скобочные последовательности.
Так, например, последовательности «(())» и «()[]» являются правильными скобочными последовательностями, а последовательности «[)» и «((» таковыми не являются.
Входной файл содержит несколько строк, каждая из которых содержит последовательность символов «(», «)», «[» и «]». Для каждой из этих строк выясните, является ли она правильной скобочной последовательностью.
•	Формат входного файла (input.txt). Первая строка входного файла содержит число N (1 ≤ N ≤ 500) – число скобочных последовательностей, которые необходимо проверить. Каждая из следующих N строк содержит скобочную последовательность длиной от 1 до 104 включительно. В каждой из последовательностей присутствуют только скобки указанных выше видов.
• Формат выходного файла(output.txt).Для каждой строки входного файла (кроме первой, в которой записано число таких строк) выведите в выходной файл «YES», если соответствующая последовательность является правильной скобочной последовательностью, или «NO», если не является.


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
   cd algorithms-and-data-structures/lab4
   ```
3. Запустите программу:
   ```bash
   python src/task3.py
   ```

4. Запуск тестов:
   ```bash
   python src/test3.py
   ```
