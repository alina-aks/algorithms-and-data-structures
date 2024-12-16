import time
import os
start = time.perf_counter()

current_script_dir = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(current_script_dir, "..", "tests", "input.txt")
output_path = os.path.join(current_script_dir, "..", "tests", "output.txt")

start = time.perf_counter()

with open(input_path, "r") as k:
    b = k.readline().split(" ")
    s = [int(l) for l in b]
    numb = int(k.readline())
indexes = []
ind = 0
for i in range(len(s)):
    if s[i]==numb:
        indexes.append(i)
        ind  = i
if ind == 0:
    ind = -1
y = open(output_path, "w")
if len(indexes)>1:
    # print("Сколько раз встречается число:",len(indexes))
    ind1 = ", ".join(str(o) for o in indexes)
    print("LAB1 Task4 answer:", ind1)
    y.write(ind1)
else:
    print("LAB1 Task4 answer:", ind)
    y.write(str(ind))


stop = time.perf_counter()
print(f"LAB1 Task4 Time: {time.perf_counter() - start}")