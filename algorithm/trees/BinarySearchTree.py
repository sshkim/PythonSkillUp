class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    root = None

    def createTree(self, arr):

        mid = len(arr) // 2

        if self.root is None:
            self.root = Node(arr[mid])

        self.createTreeNode(self.root, arr[:mid + 1])
        self.createTreeNode(self.root, arr[mid:])

    def createTreeNode(self, root, arr):
        if len(arr) < 2:
            return

        mid = len(arr) // 2

        if arr[mid] > root.key:
            root.right = Node(arr[mid])
            self.createTreeNode(root.right, arr[mid:])
        else:
            root.left = Node(arr[mid])
            self.createTreeNode(root.left, arr[:mid + 1])

    def searchNum(self, root, num):
        if root is None:
            return self.searchNum(self.root, num)

        if root.key == num:
            return True
        elif root.key > num:
            return self.searchNum(root.left, num)
        else:
            return self.searchNum(root.right, num)


list_num = [1, 2, 3, 4, 5, 6, 7]

tree = BinaryTree()

tree.createTree(list_num)
answer = tree.searchNum(None, 3)

if answer:
    print("Yes")
else:
    print("No")
