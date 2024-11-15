# Практика по Алгоритмам и Cтруктурам Данных ИТМО 

Студент(ка) ИТМО,  Аксянова Алина Рустамовна 464950 
## Вариант 1

### Навигация

- [ ] [Лабараторная 1 - Сортировка вставками, выбором, пузырьковая ](lab1/README.md)
- [ ] [Лабараторная 2 - Сортировка слиянием. Метод декомпозиции ](lab2/README.md)
  
### Описание 

### Цели и задачи

- Изучить основные команды Git
- Научиться создавать и управлять репозиториями
- Освоить работу с ветками и слияниями
- Понять основы работы с удаленными репозиториями

### Технологии и инструменты

- **Git** — система контроля версий
- **GitHub** — платформа для хостинга репозиториев
- **Markdown** — язык разметки для оформления документации
- **Python** — язык программирования
- **PyCharm** - среда разработки для написания кода

### Инструкция по запуску

## Инструкции по запуску
1. Клонирование репозитория:
> git clone https://github.com/alina-aks/algorithms-and-data-structures.git

2. Перейдите в папку с проектом:
> cd algorithms-and-data-structures

3. Запуск всех лабораторных:
> for script in lab*/*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done

4. Запуск тестов
> for script in lab*/*/tests/*.py; do PYTHONPATH=$(pwd) python "$script"; done
