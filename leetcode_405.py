# 405. Convert a Number to Hexadecimal

class Solution:
    def toHex(self, num: int) -> str:
        standard = '0123456789abcdef'
        answer = ''
        if num < 0 :
            num = 4294967295 + num + 1
        while True:
            now = num % 16
            answer = standard[now] + answer
            num = num // 16
            if num == 0:
                break
        return answer