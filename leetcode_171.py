# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, s: str) -> int:
        answer = 0
        while s:
            answer = answer * 26
            if s[0] == "A":
                answer +=  1
            elif s[0] == "B":
                answer +=  2
            elif s[0] == "C":
                answer +=  3
            elif s[0] == "D":
                answer +=  4
            elif s[0] == "E":
                answer +=  5
            elif s[0] == "F":
                answer +=  6
            elif s[0] == "G":
                answer +=  7
            elif s[0] == "H":
                answer +=  8
            elif s[0] == "I":
                answer +=  9
            elif s[0] == "J":
                answer +=  10
            elif s[0] == "K":
                answer +=  11
            elif s[0] == "L":
                answer +=  12
            elif s[0] == "M":
                answer +=  13
            elif s[0] == "N":
                answer +=  14
            elif s[0] == "O":
                answer +=  15
            elif s[0] == "P":
                answer +=  16
            elif s[0] == "Q":
                answer +=  17
            elif s[0] == "R":
                answer +=  18
            elif s[0] == "S":
                answer +=  19
            elif s[0] == "T":
                answer +=  20
            elif s[0] == "U":
                answer +=  21
            elif s[0] == "V":
                answer +=  22
            elif s[0] == "W":
                answer +=  23
            elif s[0] == "X":
                answer +=  24
            elif s[0] == "Y":
                answer +=  25
            elif s[0] == "Z":
                answer +=  26
            s = s[1:]
        return answer