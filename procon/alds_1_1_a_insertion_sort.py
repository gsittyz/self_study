def insertion_sort(array, num):
    print(" ".join(map(str, array)))
    for i in range(1, num):
        right_val = array[i]
        j = i - 1
        while j >= 0 and array[j] > right_val:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = right_val
        print(" ".join(map(str, array)))


def main():
    num = int(input())
    array = input()
    array = list(map(int, array.split()))
    insertion_sort(array, num)
    # insertion_sort([5, 2, 4, 6, 1, 3], 6)


if __name__ == "__main__":
    main()
