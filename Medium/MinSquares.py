# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
# which sum to n.

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

import math

class Solution(object):
    def numSquares(self, n):
        if n == 0:
            return 0
        # edge case, exit immediately if n is a perfect square
        squares = sorted(set([int(math.pow(i, 2)) for i in range(1,  int((math.sqrt(n))) + 1)]))
        if n in squares:
            return 1

        # the worst case is just 1*n. Initialize our array to start with this.
        opt = [i for i in range(0,n+1)]

        for i in range(2, len(opt)):
            currentMin = opt[i]

            # for candidateNum in range(1, int(math.sqrt(n)) + 1):
            #     currentSquare = int(math.pow(candidateNum, 2))
            for currentSquare in squares:
                if currentSquare > i:
                    break
                if (i - currentSquare) >= 0:
                    if opt[i - currentSquare] + 1 < currentMin:
                        currentMin = opt[i - currentSquare] + 1
                if currentMin == 1:
                    break
            opt[i] = currentMin

        return opt[n]

sol = Solution()
print(sol.numSquares(41))