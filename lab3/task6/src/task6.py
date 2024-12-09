import time
import random
import os
from lab3.utils import inp, outp, caption

CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_SCRIPT_DIR)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')

def random_quick_sort(A, left, right):
    if left < right:
        n = random.randint(left, right)
        A[right], A[n] = A[n], A[right]
        k1, k2 = partition3(A, left, right)
        random_quick_sort(A, left, k1 - 1)
        random_quick_sort(A, k2 + 1, right)
    return A

def partition3(A, left, right):
    x = A[left]
    smaller_x = left + 1
    bigger_x = right
    current = left + 1

    while current <= bigger_x:
        if A[current] < x:
            A[smaller_x], A[current] = A[current], A[smaller_x]
            smaller_x += 1
            current += 1
        elif A[current] > x:
            A[bigger_x], A[current] = A[current], A[bigger_x]
            bigger_x -= 1
        else:
            current += 1

    A[left], A[smaller_x - 1] = A[smaller_x - 1], A[left]
    return smaller_x - 1, bigger_x

def sorting_integers(A, B):
    C = []
    for a in A:
        for b in B:
            C.append(a*b)
    random_quick_sort(C, 0, len(C) - 1)
    return sum(C[i] for i in range(0, len(C), 10))

def task1():
    n, m, A, B = inp(PATH_INPUT,0 ,'task6')
    res = str(sorting_integers(A, B))
    global task_numb
    task_numb = 6
    outp(PATH_OUTPUT, res)
    print(caption(task_numb, res))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    time = float(time.perf_counter() - start)
    print(caption(task_numb, time))

