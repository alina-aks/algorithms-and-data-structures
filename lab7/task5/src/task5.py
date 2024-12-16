import time
import os
from lab7.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def subsequence(n, a, m, b, l, c):

    posl = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    posl[i][j][k] = posl[i - 1][j - 1][k - 1] + 1
                else:
                    posl[i][j][k] = max(posl[i - 1][j][k], posl[i][j - 1][k], posl[i][j][k - 1])

    return posl[n][m][l]

def task1():
    n, a, m, b, l, c = inp(PATH_INPUT, 0, 'task5')
    res = str(subsequence(n, a, m, b, l, c))
    global task_numb
    task_numb = 5
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))
