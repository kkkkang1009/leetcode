# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r"[^\w\s]", "", s)
        s = s.lower()
        s = s.replace(" ", "", s.__len__())
        compare = s[::-1]
        return s == compare