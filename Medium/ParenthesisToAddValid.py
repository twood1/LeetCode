class Solution:
    def minAddToMakeValid(self, S):
        numUnmatchedLeft = 0
        numUnmatchedRight = 0
        for c in S:
            if c == "(":
                numUnmatchedLeft = numUnmatchedLeft+1
            elif c == ")":
                if numUnmatchedLeft == 0:
                    numUnmatchedRight = numUnmatchedRight+1
                else:
                    numUnmatchedLeft = numUnmatchedLeft-1
        return numUnmatchedRight+numUnmatchedLeft