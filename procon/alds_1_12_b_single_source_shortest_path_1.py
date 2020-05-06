
def dijkstra(adj_matrix, n):
    dist = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]

    start = 0
    dist[start] = 0
    visited[start] = True
    while True:
        for end in range(n):
            # startから出ているノードの距離を計算
            if not visited[end] and adj_matrix[start][end] > -1 and dist[start] + adj_matrix[start][end] < dist[end]:
                dist[end] = dist[start] + adj_matrix[start][end]
                parent[end] = start

        # 一番近い距離にあるノードを訪問する
        min_cost = float("inf")
        for nextnode in range(n):

            if not visited[nextnode] and dist[nextnode] < min_cost:
                min_cost = dist[nextnode]
                start = nextnode
        if min_cost == float("inf"):
            return parent, dist
        visited[start] = True


def main():
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        row = [-1 for _ in range(n)]
        line = input().split()
        dim = int(line[1])
        for i in range(dim):
            row[int(line[2 + i * 2])] = int(line[2 + i * 2 + 1])
        adj_matrix.append(row)
    _, dist = dijkstra(adj_matrix, n)
    for i in range(n):
        print("{} {}".format(i, dist[i]))


if __name__ == "__main__":
    main()
