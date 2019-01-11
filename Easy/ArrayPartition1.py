# This code is actually slightly slower (~20 ms) on LeetCode than just simply sorting it always, but algorithmically
# the code is optimal. I'm sure with code optimization the time could be pushed down a bit.

class Solution:
    def arrayPairSum(self, nums):
        # We are told that n will have be in range [1, 10000], and that array is 2n size. Therefore,
        # the array will be of size [2, 20000].
        # Basic idea: We achieve the maximum sum if the list is sorted. Why? Because we end up pairing smaller minimums
        # with the next smallest minimum.
        # Two basic algorithms for solving:
        # 1) Sort the list. Sum the even indices (0,2,4,6,...). This is O(NlogN) time
        # 2) Since we know the range of the numbers is relatively small [-10000, 10000]
        # we can just "hash" the elements. This is called counting sort,
        # and runs in O(K) time, with K = 2*20001 = 40002. Not O(N) since N may be smaller than K.
        # The *2 above comes from the fact that we will loop over the list of size 20,001 twice.
        # Question is: for what N is NlogN <= K. We want to use sorting algorithm for when NlogN is <= 40002, and
        # other algorithm for when NlogN is slower.
        # Answer: NlogN <= 40002, N ~ <= 4750.

        if len(nums) < 4750:
            # sort it since N < 4750
            sortedList = sorted(nums)
            return sum(sortedList[::2])
        else:
            retval = 0

            counted = [0]*20001
            for num in nums:
                counted[num+10000] += 1

            chomp = 0
            for i in range(0, len(counted)):
                if counted[i] == 0:
                    continue
                if chomp == 1:
                    counted[i] = counted[i] - 1
                    chomp = 0
                if counted[i] == 0:
                    continue
                retval += ((i-10000)*int((counted[i]+1)/2))
                chomp = counted[i] % 2
            return int(retval)