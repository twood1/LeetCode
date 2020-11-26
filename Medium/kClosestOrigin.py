# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

import heapq as hp
import math


class Solution:
    def kClosest(self, points, K):
        heap = []
        for point in points:
            hp.heappush(heap, ((point[0]**2 + point[1]**2), point))
        return [hp.heappop(heap)[1] for _ in range(K)]


sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))