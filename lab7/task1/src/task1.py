import time
import os
from lab7.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')

def min_coins(money, coins):
    l = [float('inf')] * (money + 1)
    l[0] = 0

    for coin in coins:
        for j in range(coin, money + 1):
            l[j] = min(l[j], l[j - coin] + 1)

    return l[money] if l[money] != float('inf') else -1

def task1():
    n, p, b = inp(PATH_INPUT, 0, 'task1')
    res = str(min_coins(n, b))
    global task_numb
    task_numb = 1
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))
