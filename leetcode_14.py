# 14. Longest Common Prefix
class Solution:
   def longestCommonPrefix(self, strs):
       short = 99999
       shortStr = ""
       for str in strs:
           if short > len(str):
               short = len(str)
               shortStr = str

       for i in range(0, short):
           now = short-i
           valid = True
           for str in strs:
               if str[:now] != shortStr[:now]:
                   valid = False
                   break
           if valid :
               return shortStr[:now]

       return ""