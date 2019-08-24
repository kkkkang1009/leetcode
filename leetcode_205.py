# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = t[i]
            if hashMap[s[i]] != t[i]:
                return False
        hashMap = {}
        for i in range(len(t)):
            if t[i] not in hashMap:
                hashMap[t[i]] = s[i]
            if hashMap[t[i]] != s[i]:
                return False
        return True

# 1st - Time Limit Exceeded
# def isIsomorphic(self, s: str, t: str) -> bool:
#     list1 = list(s)
#     count = 1
#     for i in list1:
#         now = i
#         for j in range(0, list1.count(now)):
#             list1[list1.index(now)] = count
#         count += 1
#     list2 = list(t)
#     count = 1
#     for i in list2:
#         now = i
#         for j in range(0, list2.count(now)):
#             list2[list2.index(now)] = count
#         count += 1
#     if list1 == list2:
#         return True
#     return False
