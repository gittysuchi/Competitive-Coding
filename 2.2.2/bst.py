class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderSuccessor(root, p):
    successor = None

    while root:
        if p < root.val:
            successor = root.val
            root = root.left
        else:
            root = root.right

    return successor


# Creating the BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.right = TreeNode(8)


# Taking input
p = int(input("Enter node: "))

answer = inorderSuccessor(root, p)

if answer is not None:
    print("Inorder Successor:", answer)
else:
    print("No inorder successor")