from heapq import heappop, heappush


def kruskal(edges, v):
    nums = [i for i in range(v)]
    rank = [0 for i in range(v)]

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
    weight = 0
    while len(edges) > 0:
        w, s, t = heappop(edges)
        if not same(s, t):
            unite(s, t)
            weight += w
    return weight


def main():
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        s, t, w = map(int, input().split())
        heappush(edges, (w, s, t))
    print(kruskal(edges, v))


if __name__ == "__main__":
    main()
