import math
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class getPoints:
    def __init__(self, arr):
        self.points = []
        for item in arr:
            self.points.append(Point(item[0], item[1]))

class Solution:
    def maxPoints(self, points):
        # Early termination conditions.
        if not points:
            return 0

        if len(points) is 1:
            return 1

        # Instead of needing to check duplicate points, we can just hash the counts of points first.
        # When we go to count a specific coordinate's contribution to a line, we will use the number of points
        # at such coordinate, stored in pointsHash.
        pointsHash = {}
        for point in points:
            curkey = (point.x, point.y)
            if curkey not in pointsHash:
                pointsHash[curkey] = 1
            else:
                pointsHash[curkey] += 1

        # If we've only found one type of point, immediately return the count of points.
        if len(pointsHash) is 1:
            return list(pointsHash.values())[0]

        # Algorithm: Loop through every pair of points. A pair will always form a line. So all we need to check if...
        # 1) The slope is the same
        # 2) The intercept is the same
        # Sounds easy, but there are some catches:
        # Due to rounding of very large values, i.e., a slope of 99999999/99999998 vs 99999999/99999997, we need
        # to store exact values of the slope. This is true for the intercept too.
        # Storing exact value of a decimal value is equivalent to storing the reduced fraction's numerator and
        # denominator. Reducing a fraction is simply dividing both numer/denom by the GCD of the two numbers.
        # This algorithm runs in O(N^2) time.

        slopesPtsHash = {}
        slopesHash = {}
        currMax = 0
        for i in range(0, len(pointsHash.keys())):
            for j in range(i+1, len(pointsHash.keys())):
                point1 = list(pointsHash.keys())[i]
                point2 = list(pointsHash.keys())[j]
                xdiff = point1[0] - point2[0]
                ydiff = point1[1] - point2[1]
                gcd = math.gcd(xdiff,ydiff)
                xdiff = xdiff/gcd
                ydiff = ydiff/gcd
                if xdiff == 0:
                    # special type of slope for vertical lines
                    slope = (point1[0], "n")
                elif ydiff == 0:
                    # special type of slope for horizontal lines
                    slope = ("n", point1[1])
                else:
                    # b is computed by turning y = mx + b into a fraction. We will store the numer and denom exactly.
                    # b = y - (ydiff/xdiff)*x => b = (xdiff*y/xdiff) - (ydiff*x/xdiff) =>
                    # b = (xdiff*y - ydiff*x)/(xdiff)
                    bnumer = point1[1]*xdiff-point1[0]*ydiff
                    bdenom = xdiff
                    bgcd = math.gcd(int(bnumer), int(bdenom))
                    bnumer = bnumer/bgcd
                    bdenom = bdenom/bgcd
                    # store slope as an exact form of the numer/denom, and store b as an exact form
                    slope = (xdiff, ydiff, bnumer, bdenom)

                # if we haven't seen the slope,b before, add it into both hashes and count the number
                if slope not in slopesPtsHash:
                    slopesPtsHash[slope] = {point1: True, point2: True}
                    slopesHash[slope] =  pointsHash[point1] + pointsHash[point2]
                else:
                    # otherwise, we have seen this line. But we may have already counted the other point in the pair, so
                    # need to determine this, and count correctly.
                    if point1 not in slopesPtsHash[slope]:
                        slopesPtsHash[slope][point1] = True
                        slopesHash[slope] = slopesHash[slope] + pointsHash[point1]
                    if point2 not in slopesPtsHash[slope]:
                        slopesPtsHash[slope][point2] = True
                        slopesHash[slope] = slopesHash[slope] + pointsHash[point2]

                if slopesHash[slope] > currMax:
                    currMax = slopesHash[slope]

        return currMax

# Sol = Solution()
# # print(Sol.maxPoints([Point(1,1),Point(2,2),Point(3,3)]))
# # print(Sol.maxPoints([Point(0,0),Point(0,0)]))
# # print(Sol.maxPoints([Point(0,0),Point(94911151,94911150),Point(94911152,94911151)]))
# # print(Sol.maxPoints([Point(1,1),Point(3,2),Point(5,3),Point(4,1),Point(2,3),Point(1,4)]))
# # print(Sol.maxPoints([Point(0,1),Point(0,2),Point(0,3),Point(0,1),Point(0,3),Point(0,4)]))
# # points = getPoints([[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]).points
# # print(Sol.maxPoints(points))
#
# points = getPoints([[3,1],[12,3],[3,1],[-6,-1]])
# print(Sol.maxPoints(points.points))