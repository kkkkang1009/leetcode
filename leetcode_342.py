# 342. Power of Four

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while True:
            if num == 1:
                return True
            elif num <= 0:
                return False

            if num % 4 != 0:
                return False
            else:
                num /= 4