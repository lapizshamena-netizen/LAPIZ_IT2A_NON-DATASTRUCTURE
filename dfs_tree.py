from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeDFS:
    def __init__(self):
        self.root = None

    def build_level_order(self, values):
        if not values:
            self.root = None
            return self.root

        self.root = Node(values[0])
        queue = deque([self.root])
        idx = 1

        while queue and idx < len(values):
            current = queue[0]

            if current.left is None:
                current.left = Node(values[idx])
                queue.append(current.left)
                idx += 1
            elif current.right is None:
                current.right = Node(values[idx])
                queue.append(current.right)
                idx += 1
                queue.popleft()
            else:
                queue.popleft()

        return self.root

    def preorder(self, node, result=None):
        if result is None:
            result = []
        if node is None:
            return result
        result.append(node.value)
        self.preorder(node.left, result)
        self.preorder(node.right, result)
        return result

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node is None:
            return result
        self.inorder(node.left, result)
        result.append(node.value)
        self.inorder(node.right, result)
        return result

    def postorder(self, node, result=None):
        if result is None:
            result = []
        if node is None:
            return result
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.value)
        return result


if __name__ == "__main__":
    letters = list("SHAMENALAPIZ")
    tree = BinaryTreeDFS()
    root = tree.build_level_order(letters)

    print("PreOrder :", ", ".join(tree.preorder(root)))
    print("InOrder  :", ", ".join(tree.inorder(root)))
    print("PostOrder:", ", ".join(tree.postorder(root)))