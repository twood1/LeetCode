# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 1000
# 1 <= target <= 10^8


class Solution(object):
    def minSumOfLengths(self, arr, target):
        noSol = len(arr) + 1
        bestSolutionHash = {-1: [noSol, noSol]}
        leftPointer = 0
        rightPointer = 0
        currSum = arr[0]

        while leftPointer < len(arr):
            # keep right pointer aligned
            if (rightPointer == len(arr) - 1) and currSum == target:
                currentSize = rightPointer - leftPointer + 1
                tmplist = bestSolutionHash[leftPointer - 1] + [currentSize]
                minval = min(tmplist)
                tmplist.remove(minval)
                minval2 = min(tmplist)
                if minval + minval2 < sum(bestSolutionHash[rightPointer - 1]):
                    bestSolutionHash[rightPointer] = [minval, minval2]
                else:
                    bestSolutionHash[rightPointer] = bestSolutionHash[rightPointer - 1]
                break
            elif (rightPointer == len(arr) - 1) and currSum < target:
                bestSolutionHash[rightPointer] = bestSolutionHash[rightPointer - 1]
                break
            elif currSum == target:
                currentSize = rightPointer - leftPointer + 1
                # Constant time logic for finding the two minimum numbers in a list of size 3. 3 choose 2 = 3 statements
                tmplist = bestSolutionHash[leftPointer - 1] + [currentSize]
                minval = min(tmplist)
                tmplist.remove(minval)
                minval2 = min(tmplist)
                if minval + minval2 < sum(bestSolutionHash[rightPointer - 1]):
                    bestSolutionHash[rightPointer] = [minval, minval2]
                else:
                    bestSolutionHash[rightPointer] = bestSolutionHash[rightPointer - 1]
                leftPointer += 1
                rightPointer = min(rightPointer + 1, len(arr) - 1)
                currSum = currSum - arr[leftPointer-1] + arr[rightPointer]
            elif currSum > target:
                if leftPointer == rightPointer:
                    if leftPointer not in bestSolutionHash:
                        bestSolutionHash[leftPointer] = bestSolutionHash[leftPointer - 1]
                    leftPointer += 1
                    rightPointer += 1
                    if leftPointer < len(arr):
                        currSum = arr[leftPointer]
                else:
                    leftPointer += 1
                    currSum = currSum - arr[leftPointer - 1]
            else:
                # don't let right pointer overflow past the end
                if rightPointer not in bestSolutionHash:
                    bestSolutionHash[rightPointer] = bestSolutionHash[rightPointer - 1]
                rightPointer = min(rightPointer + 1, len(arr) - 1)
                currSum = currSum + arr[rightPointer]
        retval = sum(bestSolutionHash[len(arr) - 1])
        return -1 if retval > len(arr) else retval

sol = Solution()
print(sol.minSumOfLengths([1,7,2,3,2], 10))