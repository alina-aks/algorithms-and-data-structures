# Задание №7 по выбору : `Поиск максимального подмассива за линейное время`
Студентка ИТМО, Аксянова Алина Рустамовна  464950

## Вариант 1

## Задание 
Можно найти максимальный подмассив за линейное время, вос-пользовавшись следующими идеями. 
Начните с левого конца мас-сива и двигайтесь вправо, отсле- живая найденный к данному мо-менту максимальный подмассив. 
Зная максималь- ный подмассив массива A[1..j], распространите ответ на поиск максимального подмассива, заканчивающегося индексом j + 1, 
воспользовавшись следующим наблюдением: максимальный подмассив массива A[1..j + 1] представляет собой либо максимальный подмассив массива
A[1..j], либо подмассив A[i..j + 1] для некоторого 1 ≤ i ≤ j + 1. Определите максимальный подмассив вида A[i..j + 1] за констант-ное время, 
зная максимальный подмассив, заканчивающийся ин-дексом j. 


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
   python src/task7.py
   ```

4. Запуск тестов:
   ```bash
   python src/tesk7.py
   ```