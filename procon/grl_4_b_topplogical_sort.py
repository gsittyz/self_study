from collections import deque


def topological_sort(indeg, tonodes, v):
    nodes = deque([])
    visited = deque([])
    for i in range(v):
        if indeg[i] == 0:
            nodes.append(i)
    while len(nodes) > 0:
        i = nodes.popleft()
        visited.append(i)
        for j in tonodes[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                nodes.append(j)
    return visited


def main():
    ve = input().split()
    v, e = tuple(map(int, ve))
    indeg = [0 for _ in range(v)]
    tonodes = [[] for _ in range(v)]

    for _ in range(e):
        st = input().split()
        s, t = tuple(map(int, st))
        indeg[t] += 1
        tonodes[s].append(t)
    visited = topological_sort(indeg, tonodes, v)
    while len(visited) > 0:
        print(visited.popleft())


if __name__ == "__main__":
    main()
