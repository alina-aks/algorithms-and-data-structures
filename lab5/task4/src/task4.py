import time
import os
from lab5.utils import inp, outp, caption

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')
task_numb = 4


def heapify(arr, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.append((i, smallest))

        heapify(arr, n, smallest, swaps)


def build_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, swaps)
    return swaps


def task1():
    n, arr = inp(PATH_INPUT)
    swaps = build_heap(arr)
    res = str(len(swaps)) + "\n"
    res += "\n".join(f"{swap[0]} {swap[1]}" for swap in swaps)
    outp(PATH_OUTPUT, res.strip())
    print(caption(task_numb, res.strip()))


if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    elapsed_time = time.perf_counter() - start
    print(caption(task_numb, elapsed_time))
