import time
import random
import os
from lab5.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def tree_height(n, parents):
    tree = [[] for _ in range(n)]
    root = -1

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    def height(node):
        if not tree[node]:
            return 1
        max_height = 0
        for child in tree[node]:
            max_height = max(max_height, height(child))
        return max_height + 1 
    return height(root)

def task1():
    n, s = inp(PATH_INPUT)
    res = str(tree_height(n, s))
    global task_numb
    task_numb = 2
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))