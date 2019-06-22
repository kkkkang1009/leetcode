# 70. Climbing Stairs
class Solution:
   def climbStairs(self, n: 'int') -> 'int':
       if n == 1:
           return 1
       elif n == 0:
           return 1
       stairList = [0 for i in range(0, n+1)]
       stairList[0] = 1
       stairList[1] = 1
       for i in range(2, n+1):
           stairList[i] = stairList[i-1] + stairList[i-2]
       return stairList[n]