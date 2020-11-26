class Solution(object):
    def mctFromLeafValues(self, arr):
        bestSum = 2147483648
        for position in range(1, len(arr)):
            leftSum = 0
            rightSum = 0
            maxLeft = arr[0]
            maxRight = arr[len(arr) - 1]
            for left_i in range(1, position):
                prod_left = maxLeft * arr[left_i]
                leftSum += prod_left
                maxLeft = max(arr[left_i], maxLeft)

            for right_i in range(len(arr) - 2, position-1, -1):
                prod_right = maxRight * arr[right_i]
                rightSum += prod_right
                maxRight = max(arr[right_i], maxRight)

            currTreeSum = leftSum + rightSum + (maxLeft * maxRight)
            if currTreeSum < bestSum:
                bestSum = currTreeSum

        return bestSum

sol = Solution()
print(sol.mctFromLeafValues([6,2,4,10]))