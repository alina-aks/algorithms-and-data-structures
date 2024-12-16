import time
import random
import os
from lab3.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def dolls(n, k, dolls):
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(dolls[i])

    for group in groups:
        group.sort()

    sorted_dolls = []
    for i in range(n):
        sorted_dolls.append(groups[i % k][i // k])

    for i in range(1, n):
        if sorted_dolls[i] < sorted_dolls[i - 1]:
            return "НЕТ"
    return "ДА"

def task1():
    n, k, s = inp(PATH_INPUT,0, 'task3')
    res = str(dolls(n, k, s))
    global task_numb
    task_numb = 3
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))