#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findSuccessor(self, root):
        currentNode = root
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.val

    def deleteNode(self, root, key):
        if root == None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None and root.right == None:
                root = None
            elif root.left == None and root.right != None:
                root = root.right
            elif root.right == None and root.left != None:
                root = root.left
            else:
                replaceval = self.findSuccessor(root.right)
                root.val = replaceval
                root.right = self.deleteNode(root.right, root.val)
        return root

def printTree(root, prestring):
    if root.left is None and root.right is None:
        print(prestring+'Leaf:', root.val)
    else:
        print(prestring+'Node:', root.val)
        if root.left:
            printTree(root.left, prestring=prestring+'   ')
        if root.right:
            printTree(root.right, prestring=prestring+'   ')

leaf4 = TreeNode(val=4)
leaf6 = TreeNode(val=6)
leaf8 = TreeNode(val=8)
leaf12 = TreeNode(val=12)
leaf18 = TreeNode(val=18)
leaf21 = TreeNode(val=21)
leaf14 = TreeNode(val=14)


node5 = TreeNode(val=5, left=leaf4, right=leaf6)
node7 = TreeNode(val=7, left=node5, right=leaf8)

node15 = TreeNode(val=15, left=leaf14, right=None)
node17 = TreeNode(val=17, left=None, right=leaf18)
node20 = TreeNode(val=20, left=node17, right=leaf21)
node16 = TreeNode(val=16, left=node15, right=node20)

root = TreeNode(val=10, left=node7, right=node16)

sol = Solution()
sol.deleteNode(root, key=10)

printTree(root, '')

node1 = TreeNode(val=1)
node3 = TreeNode(val=3)
root = TreeNode(val=2, left=node1, right=node3)
sol = Solution()
sol.deleteNode(root, key=2)
printTree(root, '')