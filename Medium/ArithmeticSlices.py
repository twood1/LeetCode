class Solution(object):
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
        """
        :type A: List[int]
        :rtype: int
        """
        retval = 0
        previousSliceStart = 0
        previousSliceEnd = 1
        currentDiff = A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] - A[i-1] != currentDiff:
                previousSize = previousSliceEnd - previousSliceStart + 1
                if previousSize >= 3:
                    retval += ((previousSize - 2)**2 + (previousSize - 2)) / 2

                if i == len(A) - 1:
                    break

                currentDiff = A[i] - A[i-1]
                previousSliceStart = i - 1
                previousSliceEnd = i
                i += 1
            else:
                previousSliceEnd = i

        previousSize = previousSliceEnd - previousSliceStart + 1
        if previousSize >= 3:
            retval += ((previousSize - 2) ** 2 + (previousSize - 2)) / 2
        return int(retval)



sol = Solution()
print(sol.numberOfArithmeticSlices([1, 3, 5, 7, 9]))