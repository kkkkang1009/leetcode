# 415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        answer = ""
        big, small = num1, num2
        if float(num1) < float(num2):
            big, small = num2, num1
        big = big[::-1]
        small = small[::-1]
        upper = False
        for i in range(0, len(small)):
            now = int(small[i]) + int(big[i])
            if upper:
                now += 1
                upper = False
            if now >= 10:
                answer += str(now - 10)
                upper = True
            else:
                answer += str(now)
        for i in range(len(small), len(big)):
            now = int(big[i])
            if upper:
                now += 1
                upper = False
            if now >= 10:
                answer += str(now - 10)
                upper = True
            else:
                answer += str(now)
        if upper:
            answer += "1"

        return answer[::-1]