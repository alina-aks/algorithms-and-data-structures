import time
start = time.perf_counter()

k = open("../files/input.txt")
n = int(k.readline())
b = k.readline().split(" ")
s = [int(l) for l in b ]

def count_inverse(n, list):
    cnt = 0
    ls = list
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i]>ls[j] and i<j:
                cnt+=1
    return cnt

otv = str(count_inverse(n, s))
print(otv)
y = open("../files/output.txt", "w")
y.write(otv)

stop = time.perf_counter()
print("time: %s ms" % (stop - start))

