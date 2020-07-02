# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# Medium

# Given an array of integers nums and an integer target.
#
# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal than target.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)


class Solution(object):
    def numSubseq(self, nums, target):
        if (max(nums) * 2) <= target:
            return (2**len(nums) - 1)
        if (min(nums) * 2) >= target:
            return 0
        sortedNums = sorted(nums)
        while sortedNums[len(sortedNums) - 1] + sortedNums[0] > target:
            sortedNums.pop()

        leftPointer = 0
        rightPointer = len(sortedNums) - 1
        retval = 2 ** len(sortedNums) - 1

        while leftPointer <= rightPointer-1:
            currentMin = sortedNums[leftPointer]
            currentMax = sortedNums[rightPointer]
            while currentMin + currentMax <= target and leftPointer <= rightPointer:
                leftPointer = leftPointer + 1
                currentMin = sortedNums[leftPointer]

            currentSubarraySize = rightPointer - leftPointer + 1
            retval = retval - (2**currentSubarraySize - 1)

            while currentMin + currentMax > target and rightPointer >= leftPointer:
                rightPointer = rightPointer - 1
                currentMax = sortedNums[rightPointer]

            currentSubarraySize = rightPointer - leftPointer + 1
            retval = retval + (2**currentSubarraySize - 1)
        return retval % (10**9 + 7)






sol = Solution()
ans = sol.numSubseq([1,2,3,4,6], 8)
print(ans)