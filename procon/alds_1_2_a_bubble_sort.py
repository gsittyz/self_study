def bubble_sort(arr, n):
    count = 0
    for j in range(n - 1):
        for i in reversed(range(j, n - 1)):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
    return arr, count


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # n = 5
    # arr = [5, 3, 2, 4, 1]
    sorted_arr, count = bubble_sort(arr, n)
    print(" ".join(map(str, sorted_arr)))
    print(count)
    # print(sorted_arr)


if __name__ == "__main__":
    main()
