import time
import random
import os
from lab3.utils import inp, outp

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

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
    print("LAB3 Task4 answer:", res)
    outp(PATH_OUTPUT, res)
if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    print(f"LAB3 Task4 Time: {time.perf_counter() - start}")

