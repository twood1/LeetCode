class Solution:
    def __init__(self):
        self.sumHash = {}

    def findTargetSumWays(self, nums, S):
        nums.insert(0, 0)
        return self.num_ways_i(nums, 0, 0, S)

    def num_ways_i(self,nums, i, currSum, S):
        if i == (len(nums) - 1):
            if currSum == S:
                return 1
            else:
                return 0

        if (i, currSum) in self.sumHash:
            return self.sumHash[(i, currSum)]

        num_without = self.num_ways_i(nums, i + 1, currSum - nums[i+1], S)
        num_with = self.num_ways_i(nums, i + 1, currSum + nums[i + 1], S)
        self.sumHash[(i, currSum)] = num_with + num_without

        return self.sumHash[(i, currSum)]

sol = Solution()
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))