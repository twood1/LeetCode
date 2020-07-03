import math
import bisect
from operator import itemgetter
class Solution(object):
    def minDays(self, bloomDay, m, k):
        # If there aren't enough flowers in the first place, immediately exit w/ fail return value
        if (len(bloomDay) / k) < m:
            return -1

        if m == 1:
            currentMin = None
            for i in range(0, len(bloomDay)-k):
                if currentMin is None:
                    currentMin = min(bloomDay[0:k])
                else:
                    currentMin = min(currentMin, max(bloomDay[i:i+k]))
            return currentMin

        sortedBlooms = []
        for i in range(0, len(bloomDay)):
            sortedBlooms.append((bloomDay[i], i))

        sortedBlooms = sorted(sortedBlooms, key=itemgetter(0))
        separatingIndicies = [-1, len(sortedBlooms)]

        numBouquets = math.floor(len(bloomDay) / k)
        retval = sortedBlooms[len(sortedBlooms)-1][0]
        for i in range(len(sortedBlooms) - 1, -1, -1):
            bloomIdx = sortedBlooms[i][1]
            insIndex = bisect.bisect(separatingIndicies, sortedBlooms[i][1])
            separatingIndicies = separatingIndicies[0:(insIndex)] + \
                                 [bloomIdx] + \
                                 separatingIndicies[insIndex:len(separatingIndicies)]
            leftIdx = separatingIndicies[insIndex - 1]
            rightIdx = separatingIndicies[insIndex + 1]

            numBouquets = numBouquets - math.floor(((rightIdx - 1) - (leftIdx + 1) + 1) / k)
            numBouquets = numBouquets + \
                          math.floor(((bloomIdx - 1) - (leftIdx + 1) + 1) / k) + \
                          math.floor(((rightIdx - 1) - (bloomIdx + 1) + 1) / k)
            if numBouquets < m:
                retval = sortedBlooms[i][0]
                break
        return retval


sol = Solution()
print(sol.minDays([1,10,2,9,3,8,4,7,5,6], 4, 2))
