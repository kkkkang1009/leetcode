# 231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = True
        while True:
            if n < 1:
                result = False
                break
            elif n == 1:
                break
            elif n%2 == 0:
                n = n//2
            else:
                result = False
                break
        return result