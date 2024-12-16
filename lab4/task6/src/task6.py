import time
import random
import os
from lab4.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def process_commands(commands):
    queue = []
    min_queue = []
    results = []

    for command in commands:
        if command[0] == '+':
            n = int(command[1:])
            queue.append(n)
            while min_queue and min_queue[-1] > n:
                min_queue.pop()
            min_queue.append(n)

        elif command == '-':
            removed = queue.pop(0)
            if removed == min_queue[0]:
                min_queue.pop(0)

        elif command == '?':
            results.append(str(min_queue[0]))
    return results


def task1():
    m, commands = inp(PATH_INPUT, 0, 'task6')
    res = str(process_commands(commands))
    global task_numb
    task_numb = 6
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))