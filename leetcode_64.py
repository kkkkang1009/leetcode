# 64. Minimum Path Sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if i-1 < 0 and j-1 < 0:
                    continue
                elif i-1 < 0 and j-1 >= 0:
                    grid[i][j] += grid[i][j-1]
                elif j-1 < 0 and i-1 >= 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i-1][j] if grid[i-1][j] < grid[i][j-1] else grid[i][j-1]
        answer = grid[m-1][n-1]
        return answer