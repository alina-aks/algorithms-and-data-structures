import time
import random
import os
from lab4.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')
def postfix(n, s):
    stack = []
    if isinstance(s, list):
        s = ' '.join(s)
    els = s.split()

    for el in els:
        if el.isdigit():
            stack.append(int(el))
        else:
            b = stack.pop()
            a = stack.pop()

            if el == '+':
                stack.append(a + b)
            elif el == '-':
                stack.append(a - b)
            elif el == '*':
                stack.append(a * b)

    return stack[0]

def task1():
    n, s = inp(PATH_INPUT, 0, 'task8')
    res = str(postfix(n, s))
    global task_numb
    task_numb = 8
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))