def selection_sort(arr, n):
    count = 0
    for i in range(n):  # 0からn−1まで
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            count += 1
    return arr, count


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # n = 6
    # arr = [5, 6, 4, 2, 1, 3]
    arr, count = selection_sort(arr, n)
    print(" ".join(map(str, arr)))
    print(count)


if __name__ == "__main__":
    main()
