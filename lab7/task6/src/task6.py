import time
import os
from lab7.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def increasing_sequence(n, sequence):
    n = len(sequence)
    l = [float('inf')] * n
    parent = [-1] * n
    pos = [-1] * n

    max_len = 0
    max_index = -1

    for i, value in enumerate(sequence):
        pos_index = 0
        while pos_index < max_len and l[pos_index] < value:
            pos_index += 1

        l[pos_index] = value
        pos[pos_index] = i

        if pos_index > 0:
            parent[i] = pos[pos_index - 1]

        if pos_index + 1 > max_len:
            max_len = pos_index + 1
            max_index = i

    lis = []
    while max_index != -1:
        lis.append(sequence[max_index])
        max_index = parent[max_index]

    lis.reverse()
    return max_len, lis

def task1():
    n, b = inp(PATH_INPUT, 0, 'task6')
    res = str(increasing_sequence(n, b))
    global task_numb
    task_numb = 6
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))
