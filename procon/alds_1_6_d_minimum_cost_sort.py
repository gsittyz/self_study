def min_cost(nums, n):
    sorted_list = sorted(nums)
    global_min = sorted_list[0]
    check_list = [False] * n
    cost = 0
    for start_idx in range(n):
        if check_list[start_idx]:
            pass
        else:
            start_num = nums[start_idx]
            cycle_idx = start_idx
            cycle_count = 0
            min_num = start_num
            w_sum = 0
            while True:
                check_list[cycle_idx] = True
                cycle_num = nums[cycle_idx]
                w_sum += cycle_num
                next_idx = sorted_list.index(cycle_num)
                min_num = min(min_num, cycle_num)
                if next_idx == start_idx:
                    break
                cycle_idx = next_idx
                cycle_count += 1
            if cycle_count >= 1:
                cost1 = w_sum + (cycle_count - 1) * min_num
                cost2 = w_sum + min_num + (cycle_count + 2) * global_min
                cost += min(cost1, cost2)
    return cost


def main():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    cost = min_cost(nums, n)
    print(cost)


if __name__ == "__main__":
    main()
