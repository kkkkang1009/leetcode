# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(0, 100):
            a = list(str(n))
            temp = 0
            for j in a:
                temp += int(j) * int(j)
            n = temp
            if n == 1:
                print(n)
                return True

        return False