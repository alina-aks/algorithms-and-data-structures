import time
import os

current_script_dir = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(current_script_dir, "..", "tests", "input.txt")
output_path = os.path.join(current_script_dir, "..", "tests", "output.txt")

start = time.perf_counter()

# Открываем файл для чтения
with open(input_path, "r") as k:
    numb = int(k.readline())  # Читаем количество элементов
    b = k.readline().split(" ")  # Читаем сам список
    s = [int(l) for l in b]  # Преобразуем в список целых чисел

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

print("LAB3 Task1 answer:", otv)

y = open(output_path, "w")
y.write(list_ind+"\n")
y.write(otv)

stop = time.perf_counter()
print(f"LAB1 Task2 Time: {time.perf_counter() - start}")