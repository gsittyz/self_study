from collections import deque


def breadth_first_search(adj_matrix, n):
    distance = [0] + [-1] * (n - 1)
    searching = deque([0])
    while len(searching) > 0:
        start = searching.popleft()
        for end in range(n):
            if adj_matrix[start][end] and distance[end] == -1:
                searching.append(end)
                distance[end] = distance[start] + 1
    return distance


def main():
    n = int(input())
    adj = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        ukv = input().split()
        id = int(ukv[0])
        dim = int(ukv[1])
        if dim > 0:
            nodes = map(int, ukv[2:])
            for node in nodes:
                adj[id - 1][node - 1] = True
    distance = breadth_first_search(adj, n)
    for i in range(n):
        print("{} {}".format(i + 1, distance[i]))


if __name__ == "__main__":
    main()
