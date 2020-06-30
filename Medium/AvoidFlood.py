import heapq
class Solution(object):
    def avoidFlood(self, rains):
        lakeDictionary = {}
        for idx in range(len(rains)):
            if rains[idx] == 0:
                continue
            lake = rains[idx]
            if lake not in lakeDictionary:
                lakeDictionary[lake] = [idx]
            else:
                lakeDictionary[lake].append(idx)

        currentlyFilledLakes = set()
        nextBestLakeIdx = []
        retval = []
        for lake in rains:
            if lake > 0:
                if lake in currentlyFilledLakes:
                    return []
                else:
                    retval.append(-1)
                    currentlyFilledLakes.add(lake)
                    if len(lakeDictionary[lake]) >= 2:
                        lakeDictionary[lake].pop(0)
                        heapq.heappush(nextBestLakeIdx, lakeDictionary[lake].pop(0))
            else:
                if not nextBestLakeIdx:
                    retval.append(123)
                else:
                    lakeToDry = rains[heapq.heappop(nextBestLakeIdx)]
                    retval.append(lakeToDry)
                    currentlyFilledLakes.remove(lakeToDry)

        return retval

sol = Solution()
answer = sol.avoidFlood([2,3,0,0,3,1,0,1,0,2,2])
print(answer)
