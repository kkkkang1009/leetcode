# 67. Add Binary

class Solution:
   def addBinary(self, a: 'str', b: 'str') -> 'str':
       answer = int("0b" + a, 2) + int("0b" + b, 2)
       return format(answer, 'b')