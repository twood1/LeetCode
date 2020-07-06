class Solution(object):
    def returnMinIndex(self, num, leftPointer, rightPointer):

        minIdx = leftPointer
        numMins = 0
        isSorted = False
        for i in range(leftPointer, rightPointer):
            if int(num[i]) < int(num[minIdx]):
                minIdx = i
            if i > leftPointer and num[i] > num[i-1]:
                numMins += 1

        if numMins == (rightPointer - leftPointer):
            isSorted = True
        return minIdx, isSorted

    def minInteger(self, num, k):
        # let Gauss' sum be g(x)
        # if k >= g(len(num - 1), return the array sorted immediately.
        # You could use radix sort to make this linear time, since our digits are between 0-9 and string is finite.
        if k >= (len(num)**2 + len(num)) / 2:
            return ''.join(sorted(num))
        leftPointer = 0
        rightPointer = min(len(num), leftPointer + k + 1)
        numswapped = 0

        modifiedNum = num
        while numswapped != k and leftPointer < len(num) - 1:
            minIdx, isSorted = self.returnMinIndex(modifiedNum, leftPointer, rightPointer)
            if isSorted:
                leftPointer += 1
                continue
            modifiedNum = modifiedNum[0:leftPointer] + \
                          modifiedNum[minIdx] + \
                          modifiedNum[leftPointer:minIdx] + modifiedNum[minIdx + 1::]
            numswapped += (minIdx - leftPointer)
            leftPointer += 1
            rightPointer = min(len(num), leftPointer + (k - numswapped) + 1)
        return modifiedNum



sol = Solution()
print(sol.minInteger("9438957234785635408", 23))
#print(sol.minInteger("36789", 1000))
print(sol.minInteger("294984148179", 11))