# 441. Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        line = 1
        while True:
            if (line * (line +1) ) /2 >= n:
                # line += 1
                break
            else:
                line += 1
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
        return now -1
