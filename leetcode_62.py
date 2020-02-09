# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        big, small = m-1, n-1
        if m < n:
            big, small = small, big
        total = big + small
        answer = 1
        for i in range(total, big, -1):
            answer *= i
        for i in range(1, small+1):
            answer = answer//i
        return answer