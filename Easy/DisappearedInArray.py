# It may appear on first glance that this algorithm isn't linear, but it actually runs in 3N time, so O(N).
# The reason being, in the worst case we have 3 checks for each number:
# One check to see if it needs to be swapped, and then another check that verifies it is in the right position
# as we pass back over it after we swapped it.
# The final N set of checks is when we pass back over the array to add in elements that are not correctly indexed.
#
# The problem states that the returned array is not extra space, so this algorithm runs in O(N) time and uses O(1)
# space.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        i = 0
        while i < len(nums):
            num = nums[i]
            if nums[num-1] != num:
                toswap = nums[num-1]
                nums[num-1] = num
                nums[i] = toswap
            else:
                i = i+1

        arr = []
        for i in range(0, len(nums)):
            if nums[i] != (i+1):
                arr.append(i+1)
        return arr
