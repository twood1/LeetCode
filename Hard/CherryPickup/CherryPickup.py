class Solution:
    def gridBFSForward(self, grid, countGrid):
        endY = len(grid)-1
        endX = len(grid[0])-1
        currList = [(0, 0)]
        while currList:
            currCell = currList.pop(0)
            if currCell[0] != endY:
                idx = (currCell[0]+1, currCell[1])
                if grid[idx[0]][idx[1]] != -1:
                    countGrid[idx[0]][idx[1]] = max(countGrid[idx[0]][idx[1]],  grid[idx[0]][idx[1]] +
                                                                                countGrid[currCell[0]][currCell[1]])
                    currList.append(idx)

            if currCell[1] != endX:
                idx = (currCell[0], currCell[1]+1)
                if grid[idx[0]][idx[1]] != -1:
                    countGrid[idx[0]][idx[1]] = max(countGrid[idx[0]][idx[1]],  grid[idx[0]][idx[1]] +
                                                                                countGrid[currCell[0]][currCell[1]])
                    currList.append(idx)

            currList = list(set(currList))

        # If no path exists, just return immediately. We will check this in the main function
        if countGrid[endY][endX] == 0:
            return grid, countGrid

        # Otherwise, trace back until we reach the parent cell, zero'ing the path along the way in grid
        currIdx = (endY, endX)
        while currIdx[0] != 0 or currIdx[1] != 0:
            x, y = currIdx[1], currIdx[0]
            # If the parent cell is from above
            if y-1 >= 0:
                if (grid[y][x] + countGrid[y-1][x]) == countGrid[y][x]:
                    currIdx = (y-1, x)

            if x-1 >= 0:
                if (grid[y][x] + countGrid[y][x-1] == countGrid[y][x]):
                    currIdx = (y, x-1)

            grid[y][x] = 0

        return grid, countGrid


    def gridBFSBackwards(self, grid, countGrid):
        endY = 0
        endX = 0
        currList = [(len(grid[0])-1, len(grid)-1)]
        while currList:
            currCell = currList.pop(0)
            if currCell[0] != endY:
                idx = (currCell[0]-1, currCell[1])
                if grid[idx[0]][idx[1]] != -1:
                    countGrid[idx[0]][idx[1]] = max(countGrid[idx[0]][idx[1]],  grid[idx[0]][idx[1]] +
                                                    countGrid[currCell[0]][currCell[1]])
                    currList.append(idx)

            if currCell[1] != endX:
                idx = (currCell[0], currCell[1]-1)
                if grid[idx[0]][idx[1]] != -1:
                    countGrid[idx[0]][idx[1]] = max(countGrid[idx[0]][idx[1]],  grid[idx[0]][idx[1]] +
                                                    countGrid[currCell[0]][currCell[1]])
                    currList.append(idx)

            currList = list(set(currList))

        return countGrid


    def cherryPickup(self, grid):
        if len(grid) == 1:
            return grid[0][0]
        countGrid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        grid, countGrid = self.gridBFSForward(grid, countGrid)
        if countGrid[len(countGrid[0])-1][len(countGrid)-1] == 0:
            return 0
        countGrid = self.gridBFSBackwards(grid, countGrid)
        return countGrid[0][0]

Sol = Solution()
print(Sol.cherryPickup([[0, 1, -1],
                        [1, 0, -1],
                        [1, 1,  1]]))

Sol = Solution()
print(Sol.cherryPickup([[11]]))