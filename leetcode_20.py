# 20. Valid Parentheses

class Solution:
   def isValid(self, s):
       n = len(s)
       if n == 0:
           return True

       if n % 2 != 0:
           return False

       while '()' in s or '{}' in s or '[]' in s:
           s = s.replace('{}','').replace('()','').replace('[]','')

       if s == '':
           return True
       else:
           return False