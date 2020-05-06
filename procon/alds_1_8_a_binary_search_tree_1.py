class Node():
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


class Tree(dict):
    def __init__(self, obj={}):
        if isinstance(obj, dict):
            super().__init__(obj)
        else:
            raise TypeError
        self.root = -1

    def insert_key(self, key):
        node = Node()
        parent = -1  # targetの親
        target = self.root  # 探索中のkey
        while target != -1:
            parent = target
            if key < target:
                target = self[target].left
            else:
                target = self[target].right
        node.parent = parent
        self[key] = node
        if parent == -1:  # Tが空の場合、最上位の場合
            self.root = key
        elif key < parent:
            self[parent].left = key
        else:
            self[parent].right = key

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

    def __preorder_print(self, id):
        if id == -1:
            pass
        else:
            print(" {}".format(id), end="")
            self.__preorder_print(self[id].left)
            self.__preorder_print(self[id].right)

    def __inorder_print(self, id):
        if id == -1:
            pass
        else:
            self.__inorder_print(self[id].left)
            print(" {}".format(id), end="")
            self.__inorder_print(self[id].right)

    def __postorder_print(self, id):
        if id == -1:
            pass
        else:
            self.__postorder_print(self[id].left)
            self.__postorder_print(self[id].right)
            print(" {}".format(id), end="")

    def order_list(self, order_type):
        if order_type == 0:
            return self.__preorder(self.root)
        elif order_type == 1:
            return self.__inorder(self.root)
        else:
            return self.__postorder(self.root)

    def print(self):
        # self.__inorder_print(self.root)
        # print("\n", end="")
        # self.__preorder_print(self.root)
        # print("\n", end="")
        print(" {}".format(" ".join(map(str, self.order_list(1)))))
        print(" {}".format(" ".join(map(str, self.order_list(0)))))


def main():
    n = int(input())
    tree = Tree()
    for _ in range(n):
        operation = input()
        if operation[0] == "i":
            tree.insert_key(int(operation.split()[1]))
        else:
            tree.print()


if __name__ == "__main__":
    main()
