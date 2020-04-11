# 221. Maximal Square

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for x in range(len(matrix))]
        maxaera = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                else:
                    if dp[i][j-1] == 0:
                        width = 1
                    else:
                        width = dp[i][j-1]+1
                    dp[i][j] = width
                for k in range(i,-1,-1):
                    width = min(width,dp[k][j])
                    maxaera = max(maxaera,min(i-k+1,width)*min(i-k+1,width))
        return maxaera