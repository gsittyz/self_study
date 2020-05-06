class Node():
    def __init__(self, key, parent=None, left=None, right=None):
        # def typecheck(obj):
        #     if isinstance(obj, Node) or obj is None:
        #         return obj
        #     else:
        #         raise TypeError
        # if isinstance(key, int):
        #     self.key = key
        # else:
        #     raise TypeError
        # self.parent = typecheck(parent)
        # self.left = typecheck(left)
        # self.right = typecheck(right)
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def is_root(self):
        return self.parent is None

    def num_children(self):
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_parent(self):
        return self.parent is not None

    def __key(self, obj):
        if isinstance(obj, int):
            return obj
        if isinstance(obj, Node):
            return obj.key

    # def __eq__(self, other):
    #     if isinstance(other, Node):
    #         return self.__dict__ == other.__dict__
    #     return self.key == other

    # def __ne__(self, other):
    #     return self.key != self.__key(other)

    # def __gt__(self, other):
    #     return self.key > self.__key(other)

    # def __ge__(self, other):
    #     return self.key >= self.__key(other)

    # def __lt__(self, other):
    #     return self.key < self.__key(other)

    # def __le__(self, other):
    #     return self.key <= self.__key(other)


class Tree():
    def __init__(self, num_list=[]):
        self.root = None
        for num in num_list:
            self.insert(num)

    def is_empty(self):
        return self.root is None

    def insert(self, key):
        parent = None
        target = self.root
        while target is not None:
            parent = target
            if key < target.key:
                target = target.left
            else:
                target = target.right
        node = Node(key, parent)
        if node.is_root():
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def find(self, key):
        if self.is_empty():
            return None
        else:
            node = self.root
            while node is not None:
                if key == node.key:
                    return node
                elif key < node.key:
                    node = node.left
                else:
                    node = node.right
            return node

    def __preorder(self, node):
        if node is None:
            return []
        return [node.key] + self.__preorder(node.left) + self.__preorder(node.right)

    def __inorder(self, node):
        if node is None:
            return []
        return self.__inorder(node.left) + [node.key] + self.__inorder(node.right)

    def __postorder(self, node):
        if node is None:
            return []
        return self.__postorder(node.left) + self.__postorder(node.right) + [node.key]

    def preorder(self):
        return self.__preorder(self.root)

    def inorder(self):
        return self.__inorder(self.root)

    def postorder(self):
        return self.__postorder(self.root)

    def get_minimum(self, node):
        target = node
        while target.has_left():
            target = target.left
        return target

    def get_successor(self, node):
        target = node
        if target.has_right():
            return self.get_minimum(target.right)
        else:
            while target.has_parent():
                if target.parent.left is target:
                    return target.parent
                target = target.parent
            return None

    def delete(self, key):
        node = self.find(key)
        if node is None:
            raise ValueError
        if node.num_children() == 2:
            denode = self.get_successor(node)
        else:
            denode = node
        # denodeは片方にしかない
        if denode.has_left():
            child = denode.left
        else:
            child = denode.right

        # denodeの下から上への参照
        if child is not None:
            child.parent = denode.parent

        # denodeの上から下への参照
        if denode.is_root():
            self.root = denode
        elif denode.parent.left == denode:
            denode.parent.left = child
        else:
            denode.parent.right = child

        if denode is not node:
            node.key = denode.key
        del denode


# class Node():
#     def __init__(self, parent=None, left=None, right=None):
#         self.parent = parent
#         self.left = left
#         self.right = right


# class Tree(dict):
#     def __init__(self, obj={}):
#         if isinstance(obj, dict):
#             super().__init__(obj)
#         else:
#             raise TypeError
#         self.root = None

#     def insert_key(self, key):
#         node = Node()
#         parent = None  # targetの親
#         target = self.root  # 探索中のkey
#         while target is not None:
#             parent = target
#             if key < target:
#                 target = self[target].left
#             else:
#                 target = self[target].right
#         node.parent = parent
#         self[key] = node
#         if parent is None:  # Tが空の場合、最上位の場合
#             self.root = key
#         elif key < parent:
#             self[parent].left = key
#         else:
#             self[parent].right = key

#     def find(self, key):
#         # try:
#         #     self[key]
#         #     return True
#         # except KeyError:
#         #     return False
#         target = self.root
#         while True:
#             if target == key:
#                 return True
#             if key < target:
#                 target = self[target].left
#             else:
#                 target = self[target].right
#             if target is None:
#                 return False

#     def delete(self, key):
#         if (self[key].left is not None) and (self[key].right is not None):
#             successor_key = self[key].right
#             while self[successor_key].left is not None:
#                 successor_key = self[successor_key].left
#             # successorのすぐ上がkeyのときはkeyの下とsuccessorの上を一括処理
#             if self[successor_key].parent == key:
#                 # successorから上の参照
#                 parent_key = self[key].parent
#                 self[successor_key].parent = parent_key
#                 # successorから左の参照
#                 self[successor_key].left = self[key].left

#                 if parent_key is None:
#                     # 上からsuccessorへの参照
#                     self.root = successor_key
#                 else:
#                     # 上からsuccessorへの参照
#                     if self[self[parent_key].parent].left == parent_key:
#                         self[self[parent_key].parent].left = successor_key
#                     else:
#                         self[self[parent_key].parent].right = successor_key
#                     # 左からsuccessorへの参照
#                     key_left = self[parent_key].left
#                     self[key_left].parent = successor_key
#                 # 変更し終わったのでpopする
#                 self.pop(key)
#             else:  # keyとsuccessorが離れているとき
#                 parent_key = self[key].parent
#                 if parent_key is None:
#                     # 上からsuccessorへの参照
#                     self.root = successor_key
#                 else:
#                     # 上からsuccessorへの参照
#                     if self[parent_key].left == parent_key:
#                         self[parent_key].left = successor_key
#                     else:
#                         self[parent_key].right = successor_key

#                 left_key = self[key].left
#                 right_key = self[key].right
#                 # 左からsuccessorへの参照
#                 self[left_key].parent = successor_key
#                 # 右からsuccessorへの参照
#                 self[right_key].parent = successor_key
#                 # これで、successorへの参照は終わった
#                 # successorが移動することに伴う、移動前にくっついているノードの処理
#                 suc_parent_key = self[successor_key].parent
#                 suc_right_key = self[successor_key].right
#                 self[suc_parent_key].left = suc_right_key
#                 if suc_right_key is not None:
#                     self[suc_right_key].parent = suc_parent_key
#                 # successorからの参照を変える
#                 # successorから上の参照、左の参照、右の参照全部変わる
#                 self[successor_key] = self.pop(key)
#         else:
#             parent_key = self[key].parent
#             child_key = self[key].left
#             if child_key is None:
#                 child_key = self[key].right
#             # 上からの参照
#             if parent_key is not None:
#                 if self[parent_key].left == key:
#                     self[parent_key].left = child_key
#                 else:
#                     self[parent_key].right = child_key

#             # 下からの参照
#             if child_key is not None:
#                 self[child_key].parent = parent_key

#             # rootの設定
#             if parent_key is None:
#                 self.root = child_key

#             # keyのノードを削除
#             self.pop(key)

#         # delete_key = key
#         # if (self[key].left is not None) and (self[key].right is not None):
#         #     delete_key = self[key].right
#         #     # if delete_key is None:
#         #     #     while True:
#         #     #         delete_key = self[key].parent
#         #     #         if delete_key is None:
#         #     #             break
#         #     #         elif self[delete_key].parent.left == delete_key:
#         #     #             delete_key = delete_key.parent
#         #     #             break
#         #     # else:
#         #     while self[delete_key].left is not None:
#         #         delete_key = self[delete_key].left
#         # delete_node = self[delete_key]
#         # parent_key = delete_node.parent
#         # # これで片方にしか子がいなくなる
#         # # parentがNone（ルート）ならばrootを付け替える
#         # # 子のparentをdeletenodeのparentにする
#         # if delete_node.left is not None:
#         #     child_key = delete_node.left
#         # else:
#         #     child_key = delete_node.right
#         # if child_key is not None:
#         #     self[child_key].parent = parent_key
#         # # 親がいないときはrootとなる
#         # if parent_key is None:
#         #     self.root = child_key

#         # # 親のleft or rightをdeletenodeのleft or rightにする
#         # if delete_node.left is not None:
#         #     self[delete_node.parent].left = child_key
#         # else:
#         #     self[delete_node.parent].right = child_key
#         # # 付け替えの場合はdelete_keyのkeyは残してkeyの中身を入れる
#         # if delete_key != key:
#         #     self[delete_key] = self.pop(key)
#         # else:
#         #     self.pop(delete_key)

#     def __preorder(self, id):
#         if id is None:
#             return []
#         return [id] + self.__preorder(self[id].left) + self.__preorder(self[id].right)

#     def __inorder(self, id):
#         if id is None:
#             return []
#         return self.__inorder(self[id].left) + [id] + self.__inorder(self[id].right)

#     def __postorder(self, id):
#         if id is None:
#             return []
#         return self.__postorder(self[id].left) + self.__postorder(self[id].right) + [id]

#     def __preorder_print(self, id):
#         if id is None:
#             pass
#         else:
#             print(" {}".format(id), end="")
#             self.__preorder_print(self[id].left)
#             self.__preorder_print(self[id].right)

#     def __inorder_print(self, id):
#         if id is None:
#             pass
#         else:
#             self.__inorder_print(self[id].left)
#             print(" {}".format(id), end="")
#             self.__inorder_print(self[id].right)

#     def __postorder_print(self, id):
#         if id is None:
#             pass
#         else:
#             self.__postorder_print(self[id].left)
#             self.__postorder_print(self[id].right)
#             print(" {}".format(id), end="")

#     def order_list(self, order_type):
#         if order_type == 0:
#             return self.__preorder(self.root)
#         elif order_type == 1:
#             return self.__inorder(self.root)
#         else:
#             return self.__postorder(self.root)

#     def print(self):
#         # self.__inorder_print(self.root)
#         # print("\n", end="")
#         # self.__preorder_print(self.root)
#         # print("\n", end="")
#         print(" {}".format(" ".join(map(str, self.order_list(1)))))
#         print(" {}".format(" ".join(map(str, self.order_list(0)))))


def main():
    n = int(input())
    tree = Tree()
    for _ in range(n):
        operation = input()
        if operation[0] == "i":
            tree.insert(int(operation.split()[1]))
        elif operation[0] == "f":
            if tree.find(int(operation.split()[1])) is None:
                print("no")
            else:
                print("yes")
        elif operation[0] == "d":
            tree.delete(int(operation.split()[1]))
        else:
            print(" {}".format(" ".join(map(str, tree.inorder()))))
            print(" {}".format(" ".join(map(str, tree.preorder()))))


if __name__ == "__main__":
    main()
