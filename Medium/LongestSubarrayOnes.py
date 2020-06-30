class Solution(object):
    def longestSubarray(self, nums):
        zeroFound = False
        previousContigValid = False
        previousContigSize = 0
        currentContigSize = 0
        bestContigSize = 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                zeroFound = True
                if previousContigValid:
                    if previousContigSize + currentContigSize > bestContigSize:
                        bestContigSize = previousContigSize + currentContigSize
                elif currentContigSize > bestContigSize:
                        bestContigSize = currentContigSize
            else:
                if idx != 0:
                    if nums[idx-1] == 0:
                        previousContigSize = currentContigSize
                        currentContigSize = 0
                        if idx > 1:
                            if nums[idx - 2] == 1:
                                previousContigValid = True
                            else:
                                previousContigValid = False
                currentContigSize += 1
            if previousContigValid:
                if previousContigSize + currentContigSize > bestContigSize:
                    bestContigSize = previousContigSize + currentContigSize
            elif currentContigSize > bestContigSize:
                bestContigSize = currentContigSize
        if not zeroFound:
            bestContigSize = bestContigSize - 1
        return bestContigSize

sol = Solution()
print(sol.longestSubarray([1,1,1]))