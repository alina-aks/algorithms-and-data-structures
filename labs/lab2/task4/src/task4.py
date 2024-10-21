import time

start = time.perf_counter()

k = open("../files/input.txt")
n, *list1 = map(int, k.readline().split())
k, *searchs = map(int, k.readline().split())

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

res = [binary_search(list1,search) for search in searchs ]
res = " ".join(map(str,res))
print(res)

y = open("../files/output.txt", "w")
y.write(res)

stop = time.perf_counter()
print("time: %s ms" % (stop - start))

