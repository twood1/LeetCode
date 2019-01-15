class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        rowmaxes = [0]*len(grid)
        colmaxes = [0]*len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] > rowmaxes[i]:
                    rowmaxes[i] = grid[i][j]
                if grid[i][j] > colmaxes[j]:
                    colmaxes[j] = grid[i][j]

        sum = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                sum = sum+(min(rowmaxes[i], colmaxes[j]) - grid[i][j])
        return sum