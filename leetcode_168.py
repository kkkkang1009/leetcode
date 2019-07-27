# 168. Excel Sheet Column Title

class Solution:
    def convertToTitle(self, n: int) -> str:
        count = []
        while n > 26:
            count.append(n%26)
            n = n//26
        count.append(n)
        count = count[::-1]
        for i in range(len(count)-1, 0, -1):
            if count[i] == 0:
                count[i-1] -= 1
                count[i] += 26
        str = ""
        while count:
            v = count[0]
            if v == 1:
                str += "A"
            elif v == 2:
                str += "B"
            elif v == 3:
                str += "C"
            elif v == 4:
                str += "D"
            elif v == 5:
                str += "E"
            elif v == 6:
                str += "F"
            elif v == 7:
                str += "G"
            elif v == 8:
                str += "H"
            elif v == 9:
                str += "I"
            elif v == 10:
                str += "J"
            elif v == 11:
                str += "K"
            elif v == 12:
                str += "L"
            elif v == 13:
                str += "M"
            elif v == 14:
                str += "N"
            elif v == 15:
                str += "O"
            elif v == 16:
                str += "P"
            elif v == 17:
                str += "Q"
            elif v == 18:
                str += "R"
            elif v == 19:
                str += "S"
            elif v == 20:
                str += "T"
            elif v == 21:
                str += "U"
            elif v == 22:
                str += "V"
            elif v == 23:
                str += "W"
            elif v == 24:
                str += "X"
            elif v == 25:
                str += "Y"
            elif v == 26:
                str += "Z"
            count.pop(0)
        return str