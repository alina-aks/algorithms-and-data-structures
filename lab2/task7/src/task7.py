import time
start = time.perf_counter()
from lab2.utils import inp, outp

PATH_INPUT = '../files/input.txt'
PATH_OUTPUT = '../files/output.txt'

def find_max_sum(list):
    max_sum = float("-inf")
    summ, start_index, end_index = 0, 0, -1
    temp_start_index = 0
    for i in range(len(list)):
        summ += list[i]
        if summ > max_sum:
            max_sum = summ
            start_index = temp_start_index
            end_index = i
        if summ < 0:
            summ = 0
            temp_start_index = i + 1
    if max_sum < 0:
        return []
    return list[start_index:end_index+1]

def task7():
    n, s = inp(PATH_INPUT)
    res = str(find_max_sum(s))
    outp(PATH_OUTPUT, res)

if __name__ == "__main__":
    start = time.perf_counter()
    task7()
    print(f"Time: {time.perf_counter() - start}")