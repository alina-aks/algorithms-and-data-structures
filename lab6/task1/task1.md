# Задание №1 : `Множество`
Студентка ИТМО, Аксянова Алина Рустамовна  464950

## Вариант -

## Задание 
Реализуйте множество с операциями «добавление ключа», «удаление ключа», «проверка существования ключа».
• Формат входного файла (input.txt). В первой строке входного файла находится строго положительное целое число операций N, не превышающее
5 · 105. В каждой из последующих N строк находится одна из следующих операций:
A x – добавить элемент x в множество. Если элемент уже есть в множестве, то ничего делать не надо.
D x – удалить элемент x. Если элемента x нет, то ничего делать не надо.
?x–еслиключxестьвмножестве,выведите«Y»,еслинет,товыведите «N».
Аргументы указанных выше операций – целые числа, не превышающие по модулю 1018.
Формат выходного файла (output.txt). Выведите последовательно результат выполнения всех операций «?». Следуйте формату выходного файла из примера.


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
   cd algorithms-and-data-structures/lab5
   ```
3. Запустите программу:
   ```bash
   python src/task1.py
   ```

4. Запуск тестов:
   ```bash
   python src/test1.py
   ```