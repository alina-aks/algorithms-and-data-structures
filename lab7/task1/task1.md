# Задание №1 по выбору : `Обмен монет`
Студентка ИТМО, Аксянова Алина Рустамовна  464950

## Вариант 1

## Задание 
Как мы уже поняли из лекции, не всегда "жадное"решение задачи на обмен монет работает корректно для разных наборов номиналов мо-нет. Например, если доступны номиналы 1, 3 и 4, жадный алгоритм поменяет 6 центов, используя три монеты (4 + 1 + 1), в то время как его можно изменить, используя всего две монеты (3 + 3). Теперь ваша цель - применить динамическое программирование для решения зада-чи про обмен монет для разных номиналов. 
Формат ввода / входного файла (input.txt). Целое число money (1 ≤ money ≤ 103). Набор монет: количество возможных монет k и сам набор coins = {coin1, ..., coink}. 1 ≤ k ≤ 100, 1 ≤ coini ≤ 103. Проверку можно сделать на наборе {1,3,4}. Формат ввода: первая строка содержит через пробел money и k; вторая - coin1coin2...coink. 
Форматвыво-да/выходногофайла(output.txt).Вывестиодночисло–ми- ни-мальное количество необходимых монет для размена money до-ступным набором монет coins. 


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
   cd algorithms-and-data-structures/lab7
   ```
3. Запустите программу:
   ```bash
   python src/task1.py
   ```

4. Запуск тестов:
   ```bash
   python src/test1.py
   ```
