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
test_list = [24, 44, 3, 23, 1]
n = len(test_list)
print(merge_sort(test_list))