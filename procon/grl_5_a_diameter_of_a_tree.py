from heapq import heapify, heappop, heappush, heappushpop, heapreplace


def diameter(tonodes, n):
    visited = [False for _ in range(n)]
    queue = []
    max_weight = 0
    max_node = 0
    for i, node in enumerate(tonodes):
        if len(node) > 0:
            visited[i] = True
            max_node = i
            for edge in node:
                heappush(queue, (-edge[0], edge[1]))
            break

    while len(queue) > 0:
        weight, node = heappop(queue)
        visited[node] = True
        if max_weight < -weight:
            max_weight = -weight
            max_node = node
        for edge in tonodes[node]:
            if not visited[edge[1]]:
                heappush(queue, (weight - edge[0], edge[1]))

    for i in range(n):
        visited[i] = False

    visited[max_node] = True

    for edge in tonodes[max_node]:
        heappush(queue, (-edge[0], edge[1]))

    max_weight = 0

    while len(queue) > 0:
        weight, node = heappop(queue)
        visited[node] = True
        if max_weight < -weight:
            max_weight = -weight
            max_node = node
        for edge in tonodes[node]:
            if not visited[edge[1]]:
                heappush(queue, (weight - edge[0], edge[1]))

    return max_weight


def main():
    n = int(input())
    tonodes = [[] for _ in range(n)]
    for _ in range(n - 1):
        s, t, w = map(int, input().split())
        tonodes[s].append((w, t))
        tonodes[t].append((w, s))
    max_weight = diameter(tonodes, n)
    print(max_weight)


if __name__ == "__main__":
    main()
