from collections import deque


def bfs(adj_list, n):
    color = [None] * n
    color_count = 0
    searching = deque()
    for i in range(n):
        if color[i] is None:
            color_count += 1
            color[i] = color_count
            searching.append(i)
            while len(searching) > 0:
                start = searching.popleft()
                for end in adj_list[start]:
                    if color[end] is None:
                        color[end] = color_count
                        searching.append(end)
    return color


def dfs(adj_list, n):
    color = [None] * n
    color_count = 0
    searching = deque()
    for i in range(n):
        if color[i] is None:
            color_count += 1
            color[i] = color_count
            searching.append(i)
            while len(searching) > 0:
                start = searching.pop()
                for end in adj_list[start]:
                    if color[end] is None:
                        color[end] = color_count
                        searching.append(end)
    return color


def main():
    nm = input().split()
    n, m = list(map(int, nm))
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        st = input().split()
        s, t = list(map(int, st))
        adj_list[s].append(t)
        adj_list[t].append(s)
    color = bfs(adj_list, n)  # color = dfs(adj_list, n)
    q = int(input())
    for _ in range(q):
        st = input().split()
        s, t = list(map(int, st))
        if color[s] == color[t]:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
