# 66. Plus One
class Solution:
   def plusOne(self, digits: 'List[int]') -> 'List[int]':
       sum = 0
       newDigits = []
       for i in range(0, len(digits)):
           sum = sum*10 + digits[i]
       sum += 1
       str = sum.__str__()
       for i in range(0, len(str)):
           newDigits.append(int(str[i]))
       return newDigits