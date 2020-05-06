import queue
import heapq

m = 10
queue_list = [queue.Queue() for i in range(m)]


def bucket_sort(unsorted_list):
    for el in unsorted_list:
        queue_list[el].put(el)
    sorted_list = []
    for queue_el in queue_list:
        sorted_list.extend(list(queue_el.queue))
    return sorted_list


def selection_sort(unsorted_list):
    n = len(unsorted_list)
    for j in range(n - 1):
        min = j
        for i in range(j + 1, n):
            if (unsorted_list[min] > unsorted_list[i]):
                min = i
        unsorted_list[j], unsorted_list[min] = unsorted_list[min], unsorted_list[j]
    return unsorted_list


def insertion_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        tmp = unsorted_list[i]
        j = i
        while (j > 0 and unsorted_list[j] > tmp):
            unsorted_list[j + 1] = unsorted_list[j]
            j = j - 1
        unsorted_list[j] = tmp
    return unsorted_list


def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    unsorted_flag = True
    while unsorted_flag:
        unsorted_flag = False
        for i in range(n - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i +
                                                1] = unsorted_list[i + 1], unsorted_list[i]
                unsorted_flag = True
    return unsorted_list


def merge_sort(unsorted_list):
    n = len(unsorted_list)
    half = n // 2
    left = unsorted_list[:half]
    right = unsorted_list[half:]
    return merge(left, right)


def merge(left, right):
    left_n = len(left)
    right_n = len(right)
    merged = [0] * (left_n + right_n)
    merged_idx = 0
    left_idx = 0
    right_idx = 0
    while left_idx < left_n and right_idx < right_n:
        if left[left_idx] <= right[right_idx]:
            merged[merged_idx] = left[left_idx]
            left_idx += 1
        else:
            merged[merged_idx] = right[right_idx]
            right_idx += 1
        merged_idx += 1
    if left_idx < left_n - 1:
        merged[merged_idx:] = left[left_idx:]
    elif right_idx < right_n - 1:
        merged[merged_idx:] = right[right_idx:]
    return merged


def quick_sort(unsorted_list):
    n = len(unsorted_list)
    if n == 1:
        return unsorted_list
    left_idx = 0
    right_idx = n - 1
    pivot = unsorted_list[left_idx]
    while left_idx <= right_idx:
        while unsorted_list[left_idx] < pivot:
            left_idx += 1
        while unsorted_list[right_idx] > pivot:
            right_idx -= 1
        if (left_idx <= right_idx):
            unsorted_list[left_idx], unsorted_list[right_idx] = unsorted_list[right_idx], unsorted_list[left_idx]
            left_idx += 1
            right_idx -= 1
    return quick_sort(unsorted_list[:left_idx]) + quick_sort(unsorted_list[left_idx:])


def quick_sort_unrecursive(unsorted_list):
    stack = []
    n = len(unsorted_list)
    stack.append({"left": 0, "right": n - 1})
    while stack != []:
        intvl = stack.pop()
        left_idx = intvl["left"]
        right_idx = intvl["right"]
        pivot = unsorted_list[left_idx]
        while left_idx <= right_idx:
            while unsorted_list[left_idx] < pivot:
                left_idx += 1
            while unsorted_list[right_idx] > pivot:
                right_idx -= 1
            if (left_idx <= right_idx):
                unsorted_list[left_idx], unsorted_list[right_idx] = unsorted_list[right_idx], unsorted_list[left_idx]
                left_idx += 1
                right_idx -= 1
        if intvl["left"] < left_idx - 1:
            stack.append({"left": intvl["left"], "right": left_idx - 1})
        if left_idx < intvl["right"]:
            stack.append({"left": left_idx, "right": intvl["right"]})
    return unsorted_list


def heap_sort(unsorted_list):
    heapq.heapify(unsorted_list)
    return [heapq.heappop(unsorted_list) for _ in range(len(unsorted_list))]


unsorted_list = [1, 2, 3, 4, 5, 1, 4, 5, 6, 6, 7, 3, 5, 3, 6, 8, 0, 1, 2, 3, 6, 8, 9, 3, 9, 6, 4, 1, 9]

print(selection_sort(unsorted_list))
print(insertion_sort(unsorted_list))
print(bubble_sort(unsorted_list))
print(merge_sort(unsorted_list))
print(quick_sort(unsorted_list))
print(quick_sort_unrecursive(unsorted_list))
print(heap_sort(unsorted_list))


def bucket_sort_dict_like(unsorted_list):
    for el in unsorted_list:
        queue_list[el].put(el)
    sorted_list = []
    for queue_el in queue_list:
        sorted_list.extend(list(queue_el.queue))
    return sorted_list
