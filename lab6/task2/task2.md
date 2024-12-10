# Задание №2 : `Телефонная книга`
Студентка ИТМО, Аксянова Алина Рустамовна  464950

## Вариант -

## Задание 
В этой задаче ваша цель - реализовать простой менеджер телефонной книги. Он должен уметь обрабатывать следующие типы пользовательских запросов:
add number name – это команда означает, что пользователь добавляет в телефонную книгу человека с именем name и номером телефона number. Если пользователь с таким номером уже существует, то ваш менеджер должен перезаписать соответствующее имя.
del number – означает, что менеджер должен удалить человека с номером из телефонной книги. Если такого человека нет, то он должен просто игнорировать запрос.
find number – означает, что пользователь ищет человека с номером телефона number. Менеджер должен ответить соответствующим именем или строкой «not found» (без кавычек), если такого человека в книге нет. • Формат ввода / входного файла (input.txt). В первой строке входного файла содержится число N (1 ≤ N ≤ 105) - количество запросов. Далее следуют N строк, каждая из которых содержит один запрос в формате, описанном выше.
Все номера телефонов состоят из десятичных цифр, в них нет нулей в начале номера, и каждый состоит не более чем из 7 цифр. Все имена представляют собой непустые строки из латинских букв, каждая из которых имеет длину не более 15. Гарантируется при проверке, что не будет человека с именем «not found».
Формат вывода / выходного файла (output.txt). Выведите результат каждого поискового запроса find – имя, соответствующее номеру телефона, или «not found» (без кавычек), если в телефонной книге нет человека с таким номером телефона. Выведите по одному результату в каждой строке в том же порядке, как были заданы запросы типа find во входных данных.


## Ограничения по времени и памяти

- Ограничение по времени. 6сек.
- Ограничение по памяти. 512 мб.


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
   python src/task2.py
   ```

4. Запуск тестов:
   ```bash
   python src/test2.py
   ```