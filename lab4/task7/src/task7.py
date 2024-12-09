import time
import random
import os
from lab4.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')

def moving_equence_maximum(n, s, m):
    q = []
    result = []

    for i in range(n):
        if q and q[0] < i - m + 1:
            q.pop(0)
        while q and s[q[-1]] < s[i]:
            q.pop()
        q.append(i)
        if i >= m - 1:
            result.append(s[q[0]])
    return result

def task1():
    n, s, m = inp(PATH_INPUT, 0, 'task7')
    res = str(moving_equence_maximum(n, s, m))
    global task_numb
    task_numb = 7
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))