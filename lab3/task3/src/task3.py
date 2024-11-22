import time
import random
import os
from lab3.utils import inp, outp

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

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
    print("LAB3 Task3 answer:", res)
    outp(PATH_OUTPUT, res)

if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    print(f"LAB3 Task3 Time: {time.perf_counter() - start}")