def main():
    n, k = map(int, input().split())
    pp = list(map(int, input().split()))
    i = 0
    maxi = 0
    s = sum(pp[maxi:maxi + k])
    maxs = s
    while i < n - k:
        s = s - pp[i] + pp[i + k]
        if maxs < s:
            maxs = s  # 増加しているなら
            maxi = i + 1
        i += 1
    print((sum(pp[maxi:maxi + k]) + k) / 2)


if __name__ == "__main__":
    main()
