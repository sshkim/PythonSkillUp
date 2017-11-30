class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    root = None

    def __init__(self, list):
        if self.root is None:
            mid = list // 2
            self.root = Node(list[mid])

            self.create(list[:mid])
            self.create(list[mid:])

    def create(self, node=self.root, list_num=None):
        if not len(list_num):
            pass
        mid = list_num // 2
        if node.key > list_num[mid]:
            node.left = list_num[mid]
            self.create(list_num[:mid])
        else:
            node.right = list_num[mid]
            self.create(list_num[mid:])

    def search(self, node, num):
        if node.key == num:
            return True

        if node.key > num:
            search(node)



def searchTree(node, num):
    if node.key == num:
        return True
    elif node.key > num and node.left is not None:
        searchTree(node.left, num)
    elif node.right is not None:
        searchTree(node.right, num)

    return False


# m = int(input())
# list_num = list(map(int, input().trim().split(' ')))
m = 2
list_num = [1, 2, 3, 4, 5, 6, 7]

tr = Tree(list_num)
tr.search(m)
#
# def addNode(root, list):
#     if not len(list):
#         return root
#
#     mid = list // 2
#     node = Node(list[mid])
#
#     if root.key < node.key:
#         root.right = node
#         addNode(node, list[mid:])
#     else:
#         root.left = node
#         addNode(node, list[:mid])
#
#     return root


# root = addNode(None, list_num)


answer = searchTree(root, m)

if answer:
    print("Yes")
else:
    print("No")



# def add(nodes, root):
#     if root is None:
#         raise ValueError('Root is None')
#
#     # node_found = deque([root])
#     for node in nodes:



# while len(node_found) > 0:
#     current_node = node_found.popleft()
#
#     if current_node.left is None:
#         current_node.left = node
#         break
#     if current_node.right is None:
#         current_node.right = node
#         break


# root = Node(8)
# keys = [4, 12, 16, 18, 2, 1, 3]
#
# for key in keys:
#     add(Node(key), root)
