# 279. Perfect Squares

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf') ] *n
        for i in range(1, n+ 1):
            dp[i] = min(dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)) + 1
        return dp[n]

# 1st - Wrong Answer
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [sys.maxsize]*(n+4)
#         dp[0] = 0
#         for i in range(1, n+4):
#             minimum = sys.maxsize
#             for j in range(1, i+1):
#                 minimum = min(minimum, dp[i-j*j] + 1)
#                 if j*j > i:
#                     break
#             dp[i] = minimum
#         print(dp)
#         return dp[n]