import time
import random
import os
from lab5.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')

def Pyramid(n, s):
    for i in range(1, n + 1):
        if 2 * i <= n:
            if s[i - 1] > s[2 * i - 1]:
                return "NO"
        if 2 * i + 1 <= n:
            if s[i - 1] > s[2 * i]:
                return "NO"
    return "YES"

def task1():
    n, s = inp(PATH_INPUT)
    res = Pyramid(n, s)
    global task_numb
    task_numb = 1
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))