count = 0


def merge_sort(n, nums):
    if n == 1:
        return nums
    left_n = n // 2  # 左側が小さい
    left_sorted = merge_sort(left_n, nums[:left_n]) + [10**9 + 1]  # 番兵
    right_n = n - left_n
    right_sorted = merge_sort(right_n, nums[left_n:]) + [10**9 + 1]  # 番兵
    left_idx = 0
    right_idx = 0
    idx = 0
    sorted_list = [0] * n
    while idx < n:
        if left_sorted[left_idx] <= right_sorted[right_idx]:
            sorted_list[idx] = left_sorted[left_idx]
            left_idx += 1
        else:
            sorted_list[idx] = right_sorted[right_idx]
            right_idx += 1
        idx += 1
    global count
    count += idx
    return sorted_list


def main():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    sorted_list = merge_sort(n, nums)
    print(" ".join(map(str, sorted_list)))
    print(count)


if __name__ == "__main__":
    main()
