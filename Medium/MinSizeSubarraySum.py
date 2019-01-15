# Keep two pointers.

# Algorithm:
# Add current pointer 2 to the current sum.
# If current is equal or exceeds K, we know we have an interval.
#   Remove A[p1] from sum and increment p1 until interval is minimum size.
#   If the minimum sized interval is less than min interval seen, update.
#   Increment p2
# Else
#   Increment p2

class Solution:
    def minSubArrayLen(self, K, A):
        p1, p2 = 0,0
        retval = float('Inf')
        currSum = 0
        while p2 < len(A):
            currSum = currSum+A[p2]
            if currSum >= K:
                while currSum-A[p1] >= K and p1 != p2:
                    currSum = currSum - A[p1]
                    p1 = p1+1
                if p2-p1+1 < retval:
                    retval = p2-p1+1
                p2 = p2+1
            else:
                p2 = p2+1

        if retval == float('Inf'):
            retval = 0

        return retval





