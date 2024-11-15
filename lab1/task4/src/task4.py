import time
start = time.perf_counter()

k = open("../tests/input.txt")
b = k.readline().split(" ")
s = [int(l) for l in b ]
numb = int(k.readline())
indexes = []
ind = 0
for i in range(len(s)):
    if s[i]==numb:
        indexes.append(i)
        ind  = i
if ind == 0:
    ind = -1
y = open("../tests/output.txt", "w")
if len(indexes)>1:
    print("Сколько раз встречается число:",len(indexes))
    ind1 = ", ".join(str(o) for o in indexes)
    print("Индексы:",ind1)
    y.write(ind1)
else:
    print(ind)
    y.write(str(ind))

stop = time.perf_counter()
print("time: %s ms" % (stop - start))