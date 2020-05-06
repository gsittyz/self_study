import heapq


def dijkstra(adj_list, n):
    dist = [float("inf") for i in range(n)]
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    start = 0
    dist[start] = 0
    dist_heap = []  # 距離が最小のノードをすぐに探せるようにするために使う。次のノードの候補を入れる。
    heapq.heappush(dist_heap, (dist[start], start))

    while len(dist_heap) > 0:
        cost, start = heapq.heappop(dist_heap)  # 一番近いノードがスタート地点となる
        visited[start] = True
        if dist[start] < cost:  # heapのコストが最短でなければ、distを更新する必要はない
            continue
        for end, weight in adj_list[start]:
            # startから出ているノードの距離を計算してheapqに入れる
            if not visited[end] and dist[start] + weight < dist[end]:
                dist[end] = dist[start] + weight
                parent[end] = start
                heapq.heappush(dist_heap, (dist[end], end))

    return parent, dist


def main():
    n = int(input())
    adj_list = []
    for _ in range(n):
        row = []
        line = input().split()
        dim = int(line[1])
        for i in range(dim):
            row.append((int(line[2 + i * 2]), int(line[2 + i * 2 + 1])))  # 番号, 重み
        adj_list.append(row)
    _, dist = dijkstra(adj_list, n)
    for i in range(n):
        print("{} {}".format(i, dist[i]))


if __name__ == "__main__":
    main()
