import time
import os
from lab6.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def Precious_stones(n, k, s, pairs):
    beautiful_pairs = {}
    for a, b in pairs:
        if a not in beautiful_pairs:
            beautiful_pairs[a] = set()
        beautiful_pairs[a].add(b)

    stone_count = {}
    result = 0

    for i in range(n):
        current_stone = s[i]

        if current_stone in beautiful_pairs:
            for b in beautiful_pairs[current_stone]:
                if b in stone_count:
                    result += stone_count[b]

        if current_stone in stone_count:
            stone_count[current_stone] += 1
        else:
            stone_count[current_stone] = 1

    return result

def task1():
    n, k, s, l = inp(PATH_INPUT, 0, 'task7')
    res = str(Precious_stones(n, k, s, l))
    global task_numb
    task_numb = 7
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))