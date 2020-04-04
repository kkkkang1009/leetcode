# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_now = t
        for s_char in s_list:
            try:
                t_now = t_now[t_now.index(s_char)+1:]
            except ValueError as error:
                return False
        return True