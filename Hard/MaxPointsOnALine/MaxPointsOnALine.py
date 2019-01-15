# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class getPoints:
    def __init__(self, arr):
        self.points = []
        for item in arr:
            self.points.append(Point(item[0], item[1]))

import math

class Solution:
    def maxPoints(self, points):
        if not points:
            return 0

        if len(points) is 1:
            return 1

        pointsHash = {}
        for point in points:
            curkey = (point.x, point.y)
            if curkey not in pointsHash:
                pointsHash[curkey] = 1
            else:
                pointsHash[curkey] += 1

        if len(pointsHash) is 1:
            return list(pointsHash.values())[0]

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
                if xdiff != 0:
                    slope = (xdiff, ydiff)
                    invslope = (xdiff*-1, ydiff*-1)
                else:
                    invslope = None
                    slope = None
                currCount = pointsHash[point1] + pointsHash[point2]
                for k in range(0, len(pointsHash.keys())):
                    currPoint = list(pointsHash.keys())[k]
                    if currPoint == point1 or currPoint == point2:
                                        continue
                    dx1 = point1[0] - currPoint[0]
                    dy1 = point1[1] - currPoint[1]

                    if dx1 < 0 and dy1 < 0:
                        dx1, dy1 = dx1 * -1, dy1 * -1

                    gcd = math.gcd(dx1, dy1)
                    dx1 = dx1 / gcd
                    dy1 = dy1 / gcd

                    if dx1 == 0:
                        slope2 = None
                    else:
                        slope2 = (dx1, dy1)

                    if slope == slope2 or invslope == slope2:
                        currCount = currCount+pointsHash[currPoint]
                if currCount > currMax:
                    currMax = currCount
        return currMax



Sol = Solution()

print(Sol.maxPoints([Point(1,1),Point(2,2),Point(3,3)]))
print(Sol.maxPoints([Point(0,0),Point(0,0)]))
print(Sol.maxPoints([Point(0,0),Point(94911151,94911150),Point(94911152,94911151)]))
print(Sol.maxPoints([Point(1,1),Point(3,2),Point(5,3),Point(4,1),Point(2,3),Point(1,4)]))
print(Sol.maxPoints([Point(0,1),Point(0,2),Point(0,3),Point(0,1),Point(0,3),Point(0,4)]))
points = getPoints([[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]).points
print(Sol.maxPoints(points))

points = getPoints([[3,1],[12,3],[3,1],[-6,-1]])
print(Sol.maxPoints(points.points))