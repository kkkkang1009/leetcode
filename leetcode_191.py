# 191. Number of 1 Bits
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = '{:032b}'.format(n)
        count = 0
        for i in string:
            if i == '1':
                count += 1
        return count