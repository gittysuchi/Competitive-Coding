class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root, result):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root)
    inorder(root.right, result)


def inorderSuccessor(root, p):
    result = []

    # Store inorder traversal
    inorder(root, result)

    # Find the target
    for i in range(len(result)):
        if result[i].val == p:

            # Check if successor exists
            if i + 1 < len(result):
                return result[i + 1].val

            return None

    return None


# Creating the BST
root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(7)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.right = TreeNode(8)


# User input
p = int(input("Enter node: "))

answer = inorderSuccessor(root, p)

if answer is not None:
    print("Inorder Successor:", answer)
else:
    print("No inorder successor")