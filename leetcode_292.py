# 292. Nim Game

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n < 4:
            return True
        if n % 4 == 0:
            return False
        else:
            return True

