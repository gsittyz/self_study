def main():
    n, q = input().split()
    n = int(n)
    q = int(q)
    nums = [i for i in range(n)]
    rank = [0 for i in range(n)]

    def find_top(x):
        if (nums[x] != x):
            nums[x] = find_top(nums[x])
        return nums[x]

    def unite(x, y):
        x = find_top(x)
        y = find_top(y)
        if rank[x] > rank[y]:
            nums[y] = x
        else:
            nums[x] = y
            if (rank[x] == rank[y]):
                rank[y] += 1

    def same(x, y):
        return find_top(x) == find_top(y)

    for _ in range(q):
        query = input().split()
        com, x, y = tuple(map(int, query))
        if com == 0:
            unite(x, y)
        else:
            print(same(x, y) * 1)


if __name__ == "__main__":
    main()
