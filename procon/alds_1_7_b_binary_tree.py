class BinaryNode():
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
        self.depth = -1
        self.height = -1


class BinaryTree(list):
    def __init__(self, n):
        super().__init__([BinaryNode() for _ in range(n)])
        self.len = n
        self.root = None

    def set_node(self, id, left, right):
        self[id].left = left
        self[id].right = right
        if left > -1:
            self[left].parent = id
        if right > -1:
            self[right].parent = id

    def __set_depth(self, id, depth):
        self[id].depth = depth
        if self[id].left > -1:
            self.__set_depth(self[id].left, depth + 1)
        if self[id].right > -1:
            self.__set_depth(self[id].right, depth + 1)

    def set_depth(self):
        self.__set_depth(self.root, 0)

    def __set_height(self, id):
        if id == -1:
            return -1
        height = 1 + max(self.__set_height(self[id].left), self.__set_height(self[id].right))
        self[id].height = height
        return height

    def set_height(self):
        self.__set_height(self.root)

    def set_root(self):
        for i in range(self.len):
            if self[i].parent == -1:
                self.root = i
                break

    def get_nodetype(self, i):
        if self[i].parent == -1:
            return "root"
        elif self[i].left == -1 and self[i].right == -1:
            return "leaf"
        else:
            return "internal node"

    def get_sibling(self, i):
        parent = self[i].parent
        if parent == -1:
            return -1
        if self[parent].left == i:
            return self[parent].right
        else:
            return self[parent].left

    def get_degree(self, i):
        return (self[i].left > -1) * 1 + (self[i].right > -1) * 1

    def set_all(self):
        self.set_root()
        self.set_depth()
        self.set_height()

    def print(self):
        for i in range(self.len):
            print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(
                i, self[i].parent, self.get_sibling(i), self.get_degree(i),
                self[i].depth, self[i].height, self.get_nodetype(i)))


def main():
    n = int(input())
    tree = BinaryTree(n)
    for _ in range(n):
        node_info = input().split(" ")
        node_info = list(map(int, node_info))
        tree.set_node(node_info[0], node_info[1], node_info[2])
    tree.set_all()
    tree.print()


if __name__ == "__main__":
    main()
