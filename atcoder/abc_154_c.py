def main():
    n = int(input())
    aa = sorted(list(map(int, input().split())))
    i = 0
    while i < n - 1 and aa[i] != aa[i + 1]:
        i += 1
    if i == n - 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
