import sys
sys.setrecursionlimit(1000000)


class Node():
    def __init__(self, parent, child, sibling):
        self.parent = parent
        self.child = child  # 最も左の子left child
        self.sibling = sibling  # すぐ右の兄弟right sibling
        self.depth = -1

    def getnodetype(self):
        if self.parent == -1:
            return "root"
        if self.child == -1:
            return "leaf"
        return "internal node"


def setdepth(id, depth, tree):
    tree[id].depth = depth
    child = tree[id].child
    if child >= 0:
        setdepth(child, depth + 1, tree)
    sibling = tree[id].sibling
    if sibling >= 0:
        setdepth(sibling, depth, tree)


def getroot(tree, n):
    for i in range(n):
        if tree[i].parent == -1:
            return i


def getsiblings(node, tree):
    siblings = []
    sibling = node.sibling
    while sibling > -1:
        siblings.append(sibling)
        sibling = tree[sibling].sibling
    return siblings


def getchildren(node, tree):
    children = []
    child = node.child
    if child > -1:
        children.append(child)
        sibling = tree[child].sibling
        while sibling > -1:
            children.append(sibling)
            sibling = tree[sibling].sibling
    return children


def setnode(node_info, tree):
    id = node_info[0]
    dim = node_info[1]
    children = node_info[2:]
    tree[id].child = children[0]
    for i in range(dim):
        tree[children[i]].parent = id
        tree[children[i]].sibling = children[i + 1]


def printtree(tree, n):
    for i in range(n):
        node = tree[i]
        parent = node.parent
        depth = node.depth
        node_type = node.getnodetype()
        children = getchildren(node, tree)
        print("node {}: parent = {}, depth = {}, {}, [{}]".format(
            i, parent, depth, node_type, ", ".join(map(str, children))))


def main():
    n = int(input())
    tree = [Node(-1, -1, -1) for _ in range(n)]
    for _ in range(n):
        node_info = input().split(" ")
        node_info = list(map(int, node_info)) + [-1]
        setnode(node_info, tree)
    root = getroot(tree, n)
    setdepth(root, 0, tree)
    printtree(tree, n)


if __name__ == "__main__":
    main()
