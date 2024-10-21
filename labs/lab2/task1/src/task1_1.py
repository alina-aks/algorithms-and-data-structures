import time
start = time.perf_counter()

k = open("../files/input.txt")
n = int(k.readline())
b = k.readline().split(" ")
s = [int(l) for l in b ]

def merge(list1, list2):
    sorted_list = []
    l1_index = l2_index = 0
    l1_length, l2_length = len(list1), len(list2)
    for _ in range(l1_length + l2_length):
        if l1_index < l1_length and l2_index < l2_length:
            if list1[l1_index] <= list2[l2_index]:
                sorted_list.append(list1[l1_index])
                l1_index += 1
            else:
                sorted_list.append(list2[l2_index])
                l2_index += 1
        elif l1_index == l1_length:
            sorted_list.append(list2[l2_index])
            l2_index += 1
        elif l2_index == l2_length:
            sorted_list.append(list1[l1_index])
            l1_index += 1
    return sorted_list

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    list1 = merge_sort(list[:mid])
    list2 = merge_sort(list[mid:])
    return merge(list1, list2)

print(merge_sort(s))
otv = str(merge_sort(s))
y = open("../files/output.txt", "w")
y.write(otv)

stop = time.perf_counter()
print("time: %s ms" % (stop - start))