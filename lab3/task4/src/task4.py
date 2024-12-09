import time
import random
import os
from lab3.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')



def lottery(s, p, segments, points):
    result = []

    for point in points:
        count = 0
        for a, b in segments:
            if a <= point <= b:
                count += 1
        result.append(count)

    return result
def task1():
    s, p, segments, points = inp(PATH_INPUT,0 ,'task4')
    res = str(lottery(s, p, segments, points))
    global task_numb
    task_numb = 4
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))

