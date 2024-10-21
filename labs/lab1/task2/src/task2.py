import time
start = time.perf_counter()

k = open("../tests/input.txt")
numb = int(k.readline())
b = k.readline().split(" ")
s = [int(l) for l in b ]
index = [1]
for i in range(1, numb):
    elem = s[i]
    j = i
    while j >= 1 and s[j - 1] > elem:
        s[j] = s[j - 1]
        j -= 1
    index.append(j+1)
    s[j] = elem

otv = " ".join(str(t) for t in s)
list_ind = " ".join(str(o) for o in index)

print("Новые индексы:         ",list_ind)
print('Отсортированный список:', otv)

y = open("../tests/output.txt", "w")
y.write(list_ind+"\n")
y.write(otv)

stop = time.perf_counter()
print("time: %s ms" % (stop - start))