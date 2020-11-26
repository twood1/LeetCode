# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        travArray = self.inOrderTrav(root)
        print(travArray)
        swap1, swap2 = self.findswapped(travArray)
        self.replaceVal(root, swap1, swap2)
        travArray = self.inOrderTrav(root)
        print(travArray)

    def replaceVal(self, root, swap1, swap2):
        if root == None:
            return
        if root.val == swap1:
            root.val = swap2
        elif root.val == swap2:
            root.val = swap1
        self.replaceVal(root.right, swap1, swap2)
        self.replaceVal(root.left, swap1, swap2)

    def inOrderTrav(self, root):
        if root is None:
            return []
        leftarr = self.inOrderTrav(root.left)
        leftarr.append(root.val)
        rightarr = self.inOrderTrav(root.right)
        leftarr.extend(rightarr)
        return leftarr

    def findswapped(self, arr):
        leftNum = None
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                leftNum = arr[i]
                break
        print(leftNum)

        rightNum = None
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                rightNum = arr[i]
                break
        return leftNum, rightNum
leaf4 = TreeNode(val=4)
leaf6 = TreeNode(val=6)
leaf8 = TreeNode(val=8)
leaf12 = TreeNode(val=12)
leaf18 = TreeNode(val=18)
leaf21 = TreeNode(val=21)
leaf14 = TreeNode(val=14)


node5 = TreeNode(val=15, left=leaf4, right=leaf6)
node7 = TreeNode(val=7, left=node5, right=leaf8)

node15 = TreeNode(val=5, left=leaf14, right=None)
node17 = TreeNode(val=17, left=None, right=leaf18)
node20 = TreeNode(val=20, left=node17, right=leaf21)
node16 = TreeNode(val=16, left=node15, right=node20)

root = TreeNode(val=10, left=node7, right=node16)

sol = Solution()
sol.recoverTree(root)