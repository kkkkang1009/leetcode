# 172. Factorial Trailing Zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 0
        while n:
            five += n//5
            n = n//5
        return five

# 1st - Time Limit Exceeded
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         five = 0
#         while n:
#             num = n
#             while num:
#                 if num%5 == 0:
#                     five += 1
#                     num = num/5
#                 else:
#                     break
#             n = n-1
#         return five