class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findPath(root, target, path):

    if root is None:
        return False

    path.append(root)

    if root.val == target:
        return True

    if findPath(root.left, target, path):
        return True

    if findPath(root.right, target, path):
        return True

    path.pop()
    return False


def lowestCommonAncestor(root, p, q):

    path1 = []
    path2 = []

    findPath(root, p, path1)
    findPath(root, q, path2)

    i = 0

    while i < len(path1) and i < len(path2):
        if path1[i].val != path2[i].val:
            break
        i += 1

    return path1[i - 1].val


# Creating the tree
root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


# User input
p = int(input("Enter first node: "))
q = int(input("Enter second node: "))

answer = lowestCommonAncestor(root, p, q)

print("LCA:", answer)