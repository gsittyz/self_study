def main():
    n = int(input())
    m1 = input().split()
    ps = [int(m1[0]), int(m1[1])]
    for _ in range(n - 1):
        ps.append(int(input().split()[1]))
    ms = [[float("inf") for _ in range(n)] for __ in range(n)]
    # 範囲 0 - n
    for i in range(n):
        ms[i][i] = 0

    for length in range(1, n):
        # 00 11 22 33 44 ...         nn
        # 01 12 23 34 45 ...      n-1,n
        # 02 13 24 35 46 ... n-2,n
        # ...
        # 0n
        for start in range(0, n - length):
            end = start + length
            # 仕切りpartition
            m_start_end = float("inf")
            for partition in range(start, end):
                m_start_end = min(m_start_end, ms[start][partition] + ms[partition + 1]
                                  [end] + ps[start] * ps[partition + 1] * ps[end + 1])
            ms[start][end] = m_start_end
    print(ms[0][n - 1])


if __name__ == "__main__":
    main()
