from collections import deque

"""
table 1次元リスト
queenの場所 stack
queenの影響範囲 stack
table が -1 のところの8方向を調べる
queenがいたらだめ
次のところへ
queenがいなかったら
うつ
table のうち影響範囲をチェックする
全部探し終わってqueenが見つからなかったら
その前に打ったやつを戻す

"""


def nqueen(queen_rcs, n, k):
    def rc2idx(r, c):  # 7,7->88となる
        return (n + 2) * (r + 1) + c + 1

    queens = deque([])
    table = [None] * (n + 2) + ([None] + [-1] * n + [None]) * n + [None] * (n + 2)
    directions = [-(n + 3), -(n + 2), -(n + 1), -1, 1, n + 1, n + 2, n + 3]

    # queen_rcsに基づきqueenを入れ、おけない場所をマーク
    for queen_r, queen_c in queen_rcs:
        idx = rc2idx(queen_r, queen_c)
        table[idx] = idx
        for direction in directions:
            search_idx = idx
            while table[search_idx] is not None:
                if table[search_idx] == -1:
                    table[search_idx] = idx
                search_idx += direction

    idx = rc2idx(0, 0)
    max_idx = rc2idx(n - 1, n - 1)
    while len(queens) < n - k:
        # 配置できる場所を探す
        while idx <= max_idx and (table[idx] is None or table[idx] > -1):
            idx += 1
        if idx > max_idx:
            # 配置できる場所がなかった場合はバックトラック
            idx = queens.pop()
            for i in range((n + 2) * (n + 2)):
                if table[i] is not None and table[i] == idx:
                    table[i] = -1
            idx += 1
            continue
        # 配置できる場所があった場合は置く
        table[idx] = idx
        queens.append(idx)
        for direction in directions:
            search_idx = idx
            while table[search_idx] is not None:
                if table[search_idx] == -1:
                    table[search_idx] = idx
                search_idx += direction
        idx += 1
    return table


def print_table(table, n):
    def rc2idx(r, c):  # 7,7->88となる
        return (n + 2) * (r + 1) + c + 1
    for r in range(n):
        for c in range(n):
            idx = rc2idx(r, c)
            if table[idx] == idx:
                print("Q", end="")
            else:
                print(".", end="")
        print("\n", end="")


def print_table_debug(table, n):
    def rc2idx(r, c):  # 7,7->88となる
        return (n + 2) * (r + 1) + c + 1
    for r in range(n):
        for c in range(n):
            idx = rc2idx(r, c)
            if table[idx] == idx:
                print("Q", end="")
            elif table[idx] == -1:
                print(".", end="")
            else:
                print("x", end="")
        print("\n", end="")


def main():
    queen_rcs = []
    k = int(input())
    for _ in range(k):
        line = input().split()
        r, c = list(map(int, line))
        queen_rcs.append((r, c))
    table = nqueen(queen_rcs, 8, k)
    print_table(table, 8)


if __name__ == "__main__":
    main()
