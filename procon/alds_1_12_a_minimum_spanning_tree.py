# minimum_spanning_tree
def prim(adj_matrix, n):
    dist = [float("inf") for _ in range(n)]  # 訪問確定したノードからの最短距離
    visited = [False for _ in range(n)]  # ノードの訪問が確定したか
    parent = [-1 for _ in range(n)]  # start -> endを保存するためのstart？
    cost = 0
    inf = float("inf")

    start = 0
    visited[start] = True
    dist[start] = 0
    while True:
        # startから直接つながっている未訪問ノードをもとに、距離の最小値を更新する
        for end in range(n):
            if not visited[end] and adj_matrix[start][end] > -1 and adj_matrix[start][end] < dist[end]:
                dist[end] = adj_matrix[start][end]
                parent[end] = start

        min_cost = inf
        for nextnode in range(n):
            # dist_nodeの中から最もコストの短いノードを探す。そのノードは訪問確定。それを次回のstartとする。
            if not visited[nextnode] and dist[nextnode] < min_cost:
                min_cost = dist[nextnode]
                start = nextnode
        if min_cost == inf:
            break

        visited[start] = True
        cost += min_cost

    return parent, cost


def main():
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        row = input().split()
        adj_matrix.append(list(map(int, row)))
    parent, cost = prim(adj_matrix, n)
    print(cost)


if __name__ == "__main__":
    main()
