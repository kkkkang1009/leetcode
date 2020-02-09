# 28. Implement strStr()

class Solution:
   def strStr(self, haystack, needle):
       if haystack.find(needle) < 0 :
           return -1
       else :
           return haystack.find(needle)