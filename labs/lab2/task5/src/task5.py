import time
start = time.perf_counter()

k = open("../files/input.txt")
n = int(k.readline())
b = k.readline().split(" ")
list1 = [int(l) for l in b ]

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
   if list1.count(elem) > n//2:
       return True
   else:
       return False

def chek_max_el(list1):
    elem = find_max_elem(list1,0, len(list1)-1)
    if if_max(list1, elem):
        return 1
    else:
        return  0

otv = str(chek_max_el(list1))
print(otv)

y = open("../files/output.txt", "w")
y.write(otv)

stop = time.perf_counter()
print("time: %s ms" % (stop - start))