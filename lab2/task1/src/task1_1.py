import time
import os
from lab2.utils import inp, outp

current_script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_dir)

PATH_INPUT = os.path.join('..', '..', 'files', 'input.txt')
PATH_OUTPUT = os.path.join('..', '..', 'files', 'output.txt')

def merge(list1, list2):
    sorted_list = []
    l1_index = l2_index = 0
    l1_length, l2_length = len(list1), len(list2)
    for _ in range(l1_length + l2_length):
        if l1_index < l1_length and l2_index < l2_length:
            if list1[l1_index] <= list2[l2_index]:
                sorted_list.append(list1[l1_index])
                l1_index += 1
            else:
                sorted_list.append(list2[l2_index])
                l2_index += 1
        elif l1_index == l1_length:
            sorted_list.append(list2[l2_index])
            l2_index += 1
        elif l2_index == l2_length:
            sorted_list.append(list1[l1_index])
            l1_index += 1
    return sorted_list

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    list1 = merge_sort(list[:mid])
    list2 = merge_sort(list[mid:])
    return merge(list1, list2)

def task1():
    n, s = inp(PATH_INPUT)
    res = str(merge_sort(s))
    print("LAB2 Task1 answer:", res)
    outp(PATH_OUTPUT, res)

if __name__ == "__main__":
    start = time.perf_counter()
    task1()
    print(f"Time: {time.perf_counter() - start}")