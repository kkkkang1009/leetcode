# 58. Length of Last Word

class Solution:
   def lengthOfLastWord(self, s: 'str') -> 'int':
       str = ''.join(reversed(s)).strip()
       if str.find(" ") < 0:
           return len(str)
       else:
           return str.find(" ")