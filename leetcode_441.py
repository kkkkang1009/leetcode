# 441. Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        now = 1
        while True:
            n -= now
            if n == 0:
                now += 1
                break
            elif n < 0:
                n += now
                break
            now += 1
        return now - 1
