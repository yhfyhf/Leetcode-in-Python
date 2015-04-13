class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        minS = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        minS[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            print i
            minS[i][0] = minS[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            print j
            minS[0][j] = minS[0][j-1] + grid[0][j]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or j == 0:
                    pass
                else:
                    minS[i][j] = min(minS[i][j-1], minS[i-1][j]) + grid[i][j]

        return minS[i][j]
