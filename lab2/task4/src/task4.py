import time
import os
start = time.perf_counter()
from lab2.utils import inp, outp

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')

def binary_search(list1, search):
    left, right = 0, len(list1) - 1
    while left<=right:
        mid = left + (right - left) //2
        if list1[mid] == search:
            return mid
        elif list1[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def task4():
    n, list1, k, searchs = inp(PATH_INPUT)
    res = [binary_search(list1, search) for search in searchs]
    res = " ".join(map(str, res))
    print("LAB2 Task4 answer:", res)
    outp(PATH_OUTPUT, res)

if __name__ == "__main__":
    start = time.perf_counter()
    task4()
    print(f"Time: {time.perf_counter() - start}")

