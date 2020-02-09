# 38. Count and Say

class Solution:
   def countAndSay(self, n):
       if n == 1:
           return "1"
       else:
           n -= 1
           answer = "1"
           count = 0
           while count < n :
               now = ""
               nowNum = 0
               nowCount = 0
               for i in range(0, len(answer)):
                   if answer[i] == nowNum:
                       nowCount += 1
                   else :
                       if nowNum != 0:
                           now += nowCount.__str__() + nowNum.__str__()
                       nowNum = answer[i]
                       nowCount = 1
               now += nowCount.__str__() + nowNum.__str__()
               answer = now
               count += 1
           return answer