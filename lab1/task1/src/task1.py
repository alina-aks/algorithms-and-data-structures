import time
import os
start = time.perf_counter()

current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем относительные пути для input.txt и output.txt относительно текущего скрипта
input_path = os.path.join(current_script_dir, "..", "tests", "input.txt")
output_path = os.path.join(current_script_dir, "..", "tests", "output.txt")

# Открываем файл для чтения
with open(input_path, "r") as k:
    numb = int(k.readline())  # Читаем количество элементов
    b = k.readline().split(" ")  # Читаем сам список
    s = [int(l) for l in b]
for i in range(1, numb):
    elem = s[i]
    j = i
    while j >= 1 and s[j - 1] > elem:
        s[j] = s[j - 1]
        j -= 1
    s[j] = elem
otv = " ".join(str(t) for t in s)
print("LAB1 Task1 answer:", otv)

with open(output_path, "w") as y:
    y.write(otv)

stop = time.perf_counter()
print(f"LAB1 Task1 Time: {time.perf_counter() - start}")