# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class SolutionRec(object):
    def preorder(self, root):
        if root is None:
            return []
        array = [root.val]
        for child in root.children:
            array = array+self.preorder(child)
        return array

class Solution(object):
    def preorder(self, root):
        if root is None:
            return []
        array = [root.val]
        stack = list(reversed(root.children))
        while stack:
            currNode = stack.pop()
            array.append(currNode.val)
            toappend = list(reversed(currNode.children))
            [stack.append(x) for x in toappend]
        return array

Sol = Solution()
Node5 = Node(5, [])
Node6 = Node(6, [])
Node3 = Node(3, [Node5, Node6])
Node2 = Node(2, [])
Node4 = Node(4, [])
Node1 = Node(1, [Node3, Node2, Node4])
print(Sol.preorder(Node1))
