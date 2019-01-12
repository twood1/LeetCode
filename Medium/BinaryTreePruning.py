# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        if root is None:
            return None
        self.pruneHelper(root)
        return root

    # helper modifies the tree, returns true if we should keep the branch, false if not.
    def pruneHelper(self, root):
        if root is None:
            return False
        left = self.pruneHelper(root.left)
        right = self.pruneHelper(root.right)
        if not left:
            root.left = None
        if not right:
            root.right = None
        if root.val != 0:
            return True
        else:
            return left or right