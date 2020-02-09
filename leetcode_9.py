# 9. Palindrome Number

class Solution:
   def isPalindrome(self, x):
       if x < 0:
           return False
       else:
           xtoString = x.__str__()
           revX = xtoString[::-1]
           answer = int(revX)
           if answer == x:
               return True
           else:
               return False