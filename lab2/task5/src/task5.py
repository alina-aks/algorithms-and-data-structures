import time
start = time.perf_counter()
from lab2.utils import inp, outp

PATH_INPUT = '../files/input.txt'
PATH_OUTPUT = '../files/output.txt'

def find_max_elem(list1, left, right):
    if left == right:
        return list1[left]

    mid = (left + right) // 2
    left_elem = find_max_elem(list1, left, mid)
    right_elem = find_max_elem(list1, mid+1, right)

    if left_elem == right_elem:
        return left_elem

    left_cnt = sum(1 for i in range(left, right + 1) if list1[i] == left_elem)
    right_cnt = sum(1 for i in range(left, right +1 ) if list1[i] == right_elem)

    if left_cnt > right_cnt:
       return left_elem
    else:
       return right_elem

def if_max(list1, elem):
   if list1.count(elem) > len(list1)//2:
       return True
   else:
       return False

def chek_max_el(list1):
    elem = find_max_elem(list1,0, len(list1)-1)
    if if_max(list1, elem):
        return 1
    else:
        return  0

def task5():
    n, list1 = inp(PATH_INPUT)
    res = str(chek_max_el(list1))
    outp(PATH_OUTPUT, res)

if __name__ == "__main__":
    start = time.perf_counter()
    task5()
    print(f"Time: {time.perf_counter() - start}")