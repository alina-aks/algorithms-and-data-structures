import time
import random
import os
from lab3.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')


def index_harsh(citations):
    for h in range(len(citations), 0, -1):
            cnt_citation = 0
            for el in citations:
                if el >= h:
                    cnt_citation += 1
            if cnt_citation >= h:
                return h


def task1():
    s = inp(PATH_INPUT,0 ,'task5')
    res = str(index_harsh(s))
    global task_numb
    task_numb = 5
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))

if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))

