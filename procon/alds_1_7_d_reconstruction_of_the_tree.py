class BinaryNode():
    def __init__(self, parent=-1, left=-1, right=-1, depth=-1, height=-1):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
        self.height = height


class BinaryTree(list):
    def __init__(self, obj):
        if isinstance(obj, int):
            super().__init__([BinaryNode() for _ in range(obj)])
            self.len = obj
        elif isinstance(obj, list):
            super().__init__(obj)
            self.len = len(obj)
        else:
            raise TypeError("arg should be int or list of binarynodes")
        self.root = None

    # def __getitem__(self, idxs):
    #     if isinstance(idxs, tuple):
    #         return BinaryTree(list(self)[idxs])
    #     return super().__getitem__(idxs)

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

    def __preorder(self, id):
        if id == -1:
            return []
        return [id] + self.__preorder(self[id].left) + self.__preorder(self[id].right)

    def __inorder(self, id):
        if id == -1:
            return []
        return self.__inorder(self[id].left) + [id] + self.__inorder(self[id].right)

    def __postorder(self, id):
        if id == -1:
            return []
        return self.__postorder(self[id].left) + self.__postorder(self[id].right) + [id]

    def order_list(self, order_type):
        if order_type == 0:
            return self.__preorder(self.root)
        elif order_type == 1:
            return self.__inorder(self.root)
        else:
            return self.__postorder(self.root)

    def order_str(self, order_type):
        return " ".join(map(str, self.order_list(order_type)))


def get_root(preorder, inorder, num, tree):
    root = preorder[0]
    if num == 1:
        return root
    root_idx = inorder.index(root)
    left_inorder = inorder[:root_idx]
    left_preorder = preorder[1:1 + root_idx]
    left_num = root_idx
    right_inorder = inorder[root_idx + 1:]
    right_preorder = preorder[1 + root_idx:]
    right_num = num - root_idx - 1
    if left_num > 0:
        left = get_root(left_preorder, left_inorder, left_num, tree)
        if left > -1:
            tree[root].left = left
            tree[left].parent = root
    if right_num > 0:
        right = get_root(right_preorder, right_inorder, right_num, tree)
        if right > -1:
            tree[root].right = right
            tree[right].parent = root
    return root


def main():
    n = int(input())
    preorder = input().split(" ")
    preorder = list(map(lambda x: int(x) - 1, preorder))
    inorder = input().split(" ")
    inorder = list(map(lambda x: int(x) - 1, inorder))
    tree = BinaryTree(n)
    tree.root = get_root(preorder, inorder, n, tree)
    print(" ".join(map(lambda x: str(x + 1), tree.order_list(2))))


if __name__ == "__main__":
    main()
