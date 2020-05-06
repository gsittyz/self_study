def partition(array, start, end):
    end_val = array[end]
    left_end = start - 1
    for search_idx in range(start, end):
        if array[search_idx] <= end_val:
            left_end += 1
            array[left_end], array[search_idx] = array[search_idx], array[left_end]
    array[left_end + 1], array[end] = array[end], array[left_end + 1]
    return left_end + 1


def main():
    n = int(input())
    array = list(map(int, input().split(" ")))
    partition_idx = partition(array, 0, n - 1)
    array = list(map(str, array))
    print(" ".join(array[:partition_idx]) +
          " [{}] ".format(array[partition_idx]) +
          " ".join(array[partition_idx + 1:]))


if __name__ == "__main__":
    main()
