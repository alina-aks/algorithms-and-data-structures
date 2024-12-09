import time
import random
import os
from lab4.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')

def is_valid_sequence(s):
    stack = []
    matching_bracket = {')': '(', ']': '['}
    for char in s:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return "NO"
    return "YES" if not stack else "NO"

def task1():
    n, s = inp(PATH_INPUT, 0, 'task1')
    res = str([is_valid_sequence(seq) for seq in s])
    global task_numb
    task_numb = 3
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))