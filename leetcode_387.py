# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        origin = s
        count = len(s)
        now = 0
        while True:
            num = s.count(s[now])
            if num > 1:
                char = s[now]
                s = s.replace(char, "")
            else:
                now += 1
            count -= num
            if count <= now:
                break
        if s == "":
            return -1
        else:
            return origin.index(s[0])