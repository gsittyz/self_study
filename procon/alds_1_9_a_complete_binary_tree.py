def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    for i in range(n):
        print("node {}: ".format(i + 1), end="")
        print("key = {}, ".format(numbers[i]), end="")
        if i + 1 > 1:
            print("parent key = {}, ".format(numbers[(i + 1) // 2 - 1]), end="")
        if (i + 1) * 2 <= n:
            print("left key = {}, ".format(numbers[(i + 1) * 2 - 1]), end="")
        if (i + 1) * 2 + 1 <= n:
            print("right key = {}, ".format(numbers[(i + 1) * 2 + 1 - 1]), end="")
        print("\n", end="")


if __name__ == "__main__":
    main()
