import time

start = time.perf_counter()
from labs.lab2.utils import *

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


def task():
    n, list1, k, searchs = inp('../files/input.txt')
    res = [binary_search(list1, search) for search in searchs]
    res = " ".join(map(str, res))
    outp('../files/output.txt', res)
    print(res)
task()
# y = open("../files/output.txt", "w")
# y.write(res)
#
# stop = time.perf_counter()
# print("time: %s ms" % (stop - start))

