import time
start = time.perf_counter()
from lab2.utils import inp, outp

PATH_INPUT = '../files/input.txt'
PATH_OUTPUT = '../files/output.txt'

def count_inverse(n, list1):
    cnt = 0
    ls = list1
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i]>ls[j] and i<j:
                cnt+=1
    return cnt

def task3():
    n, s = inp(PATH_INPUT)
    res = str(count_inverse(n, s))
    outp(PATH_OUTPUT, res)

if __name__ == "__main__":
    start = time.perf_counter()
    task3()
    print(f"Time: {time.perf_counter() - start}")
