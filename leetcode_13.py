# 13. Roman to Integer
class Solution:
   def romanToInt(self, s):
       answer = 0
       for c in range(0, len(s)):
           if s[c].__eq__("I"):
               if c == len(s)-1:
                   answer += 1
               elif s[c+1].__eq__("V") or s[c+1].__eq__("X"):
                   answer -= 1
               else:
                   answer += 1
           elif s[c].__eq__("V"):
               answer += 5
           elif s[c].__eq__("X"):
               if c == len(s)-1:
                   answer += 10
               elif s[c+1].__eq__("L") or s[c+1].__eq__("C"):
                   answer -= 10
               else:
                   answer += 10
           elif s[c].__eq__("L"):
               answer += 50
           elif s[c].__eq__("C"):
               if c == len(s)-1:
                   answer += 100
               elif s[c+1].__eq__("D") or s[c+1].__eq__("M"):
                   answer -= 100
               else:
                   answer += 100
           elif s[c].__eq__("D"):
               answer += 500
           elif s[c].__eq__("M"):
               answer += 1000
           else:
               break;

       return answer