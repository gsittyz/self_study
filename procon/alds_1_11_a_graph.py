def conv_list(n):
    adj_matrix = []
    for _ in range(n):
        adj_list = input().split()
        adj_list = list(map(int, adj_list))
        adj_row = [0] * n
        if adj_list[1] > 0:
            for i in adj_list[2:]:
                adj_row[i - 1] = 1
        adj_matrix.append(adj_row)
    return adj_matrix


def main():
    n = int(input())
    adj_matrix = conv_list(n)
    for row in adj_matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
