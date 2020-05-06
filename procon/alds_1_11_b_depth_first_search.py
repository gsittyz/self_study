from collections import deque


def conv_list(n):
    adj_matrix = []
    for _ in range(n):
        adj_list = input().split()
        adj_list = list(map(int, adj_list))
        adj_row = [False] * n
        if adj_list[1] > 0:
            for i in adj_list[2:]:
                adj_row[i - 1] = True
        adj_matrix.append(adj_row)
    return adj_matrix


def depth_first_search(adj_matrix, n):
    visited = [None] * n
    count = 1
    searched = [None] * n
    start = 0
    stack = deque()
    stack.append(start)
    visited[start] = 1
    while count <= 2 * n:
        has_edge = adj_matrix[start]
        i = 0   
        while i < n:
            if has_edge[i] and visited[i] is None:
                stack.append(i)
                count += 1
                visited[i] = count
                break
            i += 1
        if i < n:
            start = i
        else:
            searched_node = stack.pop()
            count += 1
            searched[searched_node] = count
            if len(stack) > 0:
                start = stack[-1]
            elif count < 2 * n:
                start = visited.index(None)
                stack.append(start)
                count += 1
                visited[start] = count
            else:
                break
    return visited, searched


def main():
    n = int(input())
    adj_matrix = conv_list(n)
    visited, searched = depth_first_search(adj_matrix, n)
    for i in range(n):
        print("{} {} {}".format(i + 1, visited[i], searched[i]))


if __name__ == "__main__":
    main()
