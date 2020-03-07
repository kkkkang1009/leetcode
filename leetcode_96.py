# 96. Unique Binary Search Trees

class Solution:
    def numTrees(self, n: int) -> int:
        # catalan_num
        def calcul(num: int) -> int:
            if num == 0:
                return 1
            else:
                return calcul(num - 1) * 2 * (2 * num + 1) // (num + 2)

        return calcul(n - 1)
