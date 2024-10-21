import time
start = time.perf_counter()

k = open("../tests/input.txt")
numb = int(k.readline())
b = k.readline().split(" ")
s = [int(l) for l in b ]

for i in range(1, numb):
    elem = s[i]
    j = i
    while j >= 1 and s[j - 1] > elem:
        s[j] = s[j - 1]
        j -= 1
    s[j] = elem
otv = " ".join(str(t) for t in s)
print('Отсортированный список:', otv)

y = open("../tests/output.txt", "w")
y.write(otv)

stop = time.perf_counter()
print("time: %s ms" % (stop - start))