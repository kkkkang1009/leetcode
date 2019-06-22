# 69. Sqrt(x)
# Change scoring criteria - TimeOut
# class Solution:
#    def mySqrt(self, x: 'int') -> 'int':
#        answer = 0
#        while answer <=  x:
#            if answer*answer == x:
#                return answer
#            elif answer*answer > x:
#                break
#            else:
#                answer += 1
#        return answer-1


class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        answer = 0
        while answer <=  x:
            if answer*answer > x:
                break
            else:
                answer += 1
        return answer-1