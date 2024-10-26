import time
start = time.perf_counter()
from labs.lab2.utils import *
def count_inverse(n, list1):
    cnt = 0
    ls = list1
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i]>ls[j] and i<j:
                cnt+=1
    return cnt
def task():
    n, s = inp('../files/input.txt')
    res = str(count_inverse(n, s))
    outp('../files/output.txt', res)
    print(res)
task()
# y = open("../files/output.txt", "w")
# y.write(otv)
#
# stop = time.perf_counter()
# print("time: %s ms" % (stop - start))

