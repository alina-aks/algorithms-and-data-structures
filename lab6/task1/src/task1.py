import time
import os
from lab6.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def process_operations(n, operations):
    result = []
    set_list = set()

    for operation in operations:
        op, x = operation[0], int(operation[1])

        if op == 'A':
            set_list.add(x)
        elif op == 'D':
            set_list.discard(x)
        elif op == '?':
            result.append('Y' if x in set_list else 'N')

    return result

def task1():
    n, s = inp(PATH_INPUT, 0, 'task1')
    res = str(process_operations(n, s))
    global task_numb
    task_numb = 1
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))
