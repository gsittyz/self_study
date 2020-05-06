def min_item_num(weights, num_item, num_vehicle, capacity):
    item_idx = 0
    for _ in range(num_vehicle):
        load = 0
        while load + weights[item_idx] <= capacity:
            load += weights[item_idx]
            item_idx += 1
            if item_idx == num_item:
                return num_item
    return item_idx


def main():
    num_item, num_vehicle = list(map(int, input().split(" ")))
    weights = [int(input()) for _ in range(num_item)]
    left = 0
    right = 10000 * 100000
    while right - left > 1:
        center = (left + right) // 2
        min_item = min_item_num(weights, num_item, num_vehicle, center)
        if num_item <= min_item:
            right = center
        else:  # min_vehicle > num_item:
            left = center
    print(right)


if __name__ == "__main__":
    main()
