import time
import random
import os
from lab3.utils import inp, outp

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def anti_quick_sort(n):
    a = [i+1 for i in range(n)]
    for i in range(2, len(a)):
        a[i], a[i//2] = a[i//2], a[i]
    return a

def task1():
    n = inp(PATH_INPUT,0,'task2')
    res = str(anti_quick_sort(n))
    print("LAB3 Task2 answer:", res)
    outp(PATH_OUTPUT, res)

if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    print(f"LAB3 Task2 Time: {time.perf_counter() - start}")
