def main():
    n = int(input())
    if n <= 1:
        print(1)
    else:
        fib_list = [1, 1] + [None] * (n - 1)
        for i in range(2, n + 1):
            fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        print(fib_list[n])


if __name__ == "__main__":
    main()
