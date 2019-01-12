# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        treeHash = self.valuesHash(root, 0, {})
        maxVals = []
        for i in range(0, len(treeHash)):
            maxVals.append(max(treeHash[i]))
        return maxVals


    def valuesHash(self, root, i, hash):
        if root is None:
            return {}
        if i not in hash:
            hash[i] = [root.val]
        else:
            hash[i].append(root.val)
        self.valuesHash(root.left, i+1, hash)
        self.valuesHash(root.right, i+1, hash)

        return hash