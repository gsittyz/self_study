def max_profit(n, values):
    min_val = values[0]
    profit = -(10**9)

    for i in range(1, n):
        if profit < values[i] - min_val:
            profit = values[i] - min_val
        if min_val > values[i]:
            min_val = values[i]

    return profit


def main():
    n = int(input())
    values = [int(input()) for i in range(n)]
    print(max_profit(n, values))


if __name__ == "__main__":
    main()
