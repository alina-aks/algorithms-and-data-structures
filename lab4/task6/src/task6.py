import time
import random
import os
from lab4.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')
task_numb = 6


def process_commands(commands):
    queue = []  # Основная очередь
    min_queue = []  # Очередь для хранения минимальных элементов
    results = []

    for command in commands:
        if command[0] == '+':
            # Добавляем элемент в очередь
            n = int(command[1:])  # Все после символа '+' — это число
            queue.append(n)

            # Обновление min_queue, поддерживаем минимальные элементы в порядке возрастания
            while min_queue and min_queue[-1] > n:
                min_queue.pop()  # Убираем элементы из min_queue, которые больше n
            min_queue.append(n)

        elif command == '-':
            # Извлекаем элемент из очереди
            removed = queue.pop(0)  # Удаляем элемент с начала очереди

            # Если удаленный элемент был минимальным, удаляем его и из min_queue
            if removed == min_queue[0]:
                min_queue.pop(0)

        elif command == '?':
            # Запрашиваем минимальный элемент
            results.append(str(min_queue[0]))

    return results


def task1():
    m, commands = inp(PATH_INPUT, 0, 'task6')
    res = process_commands(commands)
    outp(PATH_OUTPUT, "\n".join(res))
    print(caption(task_numb, "\n".join(res)))
if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption( task_numb, time))