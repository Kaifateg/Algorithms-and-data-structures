from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 0


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root:
            return self._find(value, self.root)

    def _find(self, value, node):
        if value == node.value:
            return node.value
        elif value < node.value and node.left:
            return self._find(value, node.left)
        elif value > node.value and node.right:
            return self._find(value, node.right)


tree = BinaryTree()
tree.insert(3)
tree.insert(4)
tree.insert(0)
tree.insert(8)
tree.insert(2)
print(tree.find(3))
print(tree.find(10))


def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

            
bfs(tree.root)
print("  ")


def dfs_preorder(node):
    if node:
        print(node.value, end=' ')
        dfs_preorder(node.left)
        dfs_preorder(node.right)


def dfs_inorder(node):
    if node:
        dfs_inorder(node.left)
        print(node.value, end=' ')
        dfs_inorder(node.right)


def dfs_postorder(node):
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=' ')


dfs_preorder(tree.root)
print("  ")
dfs_inorder(tree.root)
print("  ")
dfs_postorder(tree.root)
print("  ")


class AVLTree(BinaryTree):
    def insert(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(
            node.right))
        balance = self.rebalance(node)

        # Left rotation
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Right rotation
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Left-Right rotation
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right-Left rotation
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def rebalance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)


tree2 = AVLTree()
root = None
values = [9, 15, 8, 5, 3]
for value in values:
    root = tree2.insert(root, value)

def pre_order(node):
    if not node:
        return
    pre_order(node.left)
    print(f"value={node.value} height={node.height},", end=" ")
    pre_order(node.right)

pre_order(root)
