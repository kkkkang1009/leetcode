# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        for char in s:
            if char not in hash:
                hash.add(char)
            else:
                hash.remove(char)
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)