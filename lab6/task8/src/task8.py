import time
import os
from lab6.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def hash_table(N, X, A, B, AC, BC, AD, BD):
    table = set()

    for _ in range(N):
        if X in table:
            A = (A + AC) % 103
            B = (B + BC) % 10 ** 15
        else:
            table.add(X)
            A = (A + AD) % 103
            B = (B + BD) % 10 ** 15

        X = (X * A + B) % 10 ** 15

    return X, A, B

def task1():
    n, x, a, b, A_c, B_c, A_d, B_d = inp(PATH_INPUT, 0, 'task8')
    res = str(hash_table(n, x, a, b, A_c, B_c, A_d, B_d))
    global task_numb
    task_numb = 8
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))