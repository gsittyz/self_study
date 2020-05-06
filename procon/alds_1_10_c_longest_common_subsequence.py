def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [0] * (n + 1)
    for i in range(1, m + 1):
        row = [0]
        x_i_1 = x[i - 1]
        for j in range(1, n + 1):
            row.append(c[j - 1] + 1 if x_i_1 == y[j - 1] else max(row[j - 1], c[j]))
        c = row
    return c[n]


def main():
    q = int(input())
    for _ in range(q):
        x = input()
        y = input()
        print(lcs(x, y))


if __name__ == "__main__":
    main()
# TLE
