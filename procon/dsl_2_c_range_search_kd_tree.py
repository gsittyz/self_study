from collections import deque


class Node():
    def __init__(self, idx, x, y, left=None, right=None):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = left
        self.right = right


def node_bisect(node_lst, left, right, on_x=True):
    if right == left:
        return None
    elif right - left == 1:
        return node_lst[left]
    else:
        mid = (left + right) // 2
        if on_x:
            node_lst[left:right] = sorted(node_lst[left:right], key=lambda node: node.x)
        else:
            node_lst[left:right] = sorted(node_lst[left:right], key=lambda node: node.y)
        node_lst[mid].left = node_bisect(node_lst, left, mid, not on_x)
        node_lst[mid].right = node_bisect(node_lst, mid + 1, right, not on_x)
    return node_lst[mid]


def search(min_x, max_x, min_y, max_y, node, on_x=True):
    idx_lst = []
    if node is not None:
        if on_x:
            if (min_x <= node.x):
                idx_lst.extend(search(min_x, max_x, min_y, max_y, node.left, not on_x))
            if (min_x <= node.x <= max_x and min_y <= node.y <= max_y):
                idx_lst.append(node.idx)
            if (node.x <= max_x):
                idx_lst.extend(search(min_x, max_x, min_y, max_y, node.right, not on_x))
        else:
            if (min_y <= node.y):
                idx_lst.extend(search(min_x, max_x, min_y, max_y, node.left, not on_x))
            if (min_x <= node.x <= max_x and min_y <= node.y <= max_y):
                idx_lst.append(node.idx)
            if (node.y <= max_y):
                idx_lst.extend(search(min_x, max_x, min_y, max_y, node.right, not on_x))
    return idx_lst


def main():
    n = int(input())
    node_lst = []
    for i in range(n):
        coord = input().split()
        x, y = tuple(map(int, coord))
        node_lst.append(Node(i, x, y))
    root = node_bisect(node_lst, 0, len(node_lst))

    q = int(input())
    for i in range(q):
        rect = input().split()
        sx, tx, sy, ty = tuple(map(int, rect))
        indices = search(sx, tx, sy, ty, root)
        if len(indices) > 0:
            indices = sorted(indices)
            for i in indices:
                print(i)
        print()


if __name__ == "__main__":
    main()
