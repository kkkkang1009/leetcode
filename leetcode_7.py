# 7. Reverse Integer
class Solution:
   def reverse(self, x):
       if x > 0:
           xtoString = x.__str__()
           revX = xtoString[::-1]
           answer = int(revX)
       else:
           x = -x
           xtoString = x.__str__()
           revX = xtoString[::-1]
           answer = -int(revX)
       if answer > 2147483647 or answer < -2147483648:
           return 0
       return answer