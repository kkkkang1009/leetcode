# 263. Ugly Number
class Solution:
    def isUgly(self, num: int) -> bool:
        now = 0
        while True:
            if now is num:
                break
            now = num
            if num % 2 is 0:
                num = num // 2
            if num % 3 is 0:
                num = num // 3
            if num % 5 is 0:
                num = num // 5
        if num == 1 :
            return True
        else:
            return False