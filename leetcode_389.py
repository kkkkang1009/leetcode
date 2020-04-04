# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        for s_char in s_list:
            t = t.replace(s_char, "", 1)
        return t