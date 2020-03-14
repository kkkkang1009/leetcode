# 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while True:
            if n * n < num:
                n += 1
            elif n * n == num:
                return True
            else:
                return False
