
from collections import deque

# Create a Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
def create_tree():
    root = Node("L")

    root.left = Node("A")
    root.right = Node("P")

    root.right.left = Node("I")
    root.right.right = Node("Z")

    return root


# BFS - Level Order Traversal
def bfs(root):
    if root is None:
        return

    queue = deque([root])

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print()


# DFS - Preorder Traversal
def dfs_preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)


# DFS - Inorder Traversal
def dfs_inorder(root):
    if root is None:
        return

    dfs_inorder(root.left)
    print(root.data, end=" ")
    dfs_inorder(root.right)


# DFS - Postorder Traversal
def dfs_postorder(root):
    if root is None:
        return

    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data, end=" ")


# MAIN METHOD
def main():
    root = create_tree()

    print("BINARY TREE - LAPIZ")
    print("-------------------")

    bfs(root)

    print("DFS Preorder:", end=" ")
    dfs_preorder(root)

    print("\nDFS Inorder:", end=" ")
    dfs_inorder(root)

    print("\nDFS Postorder:", end=" ")
    dfs_postorder(root)

    print()


if __name__ == "__main__":
    main()



