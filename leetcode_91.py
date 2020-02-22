# 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = prev1 = 1
        if s[-1] == '0':
            prev1 = 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == '1' or (s[i] == '2' and s[i+1] < '7'):
                prev1, prev2 = prev1 + prev2, prev1
            elif s[i] == '0':
                prev1, prev2 = 0, prev1
            else:
                prev2 = prev1
        return prev1

# 1st - Wrong Answer
# def numDecodings(self, s: str) -> int:
#     count = [0] * len(s)
#
#     for i in range(0, len(s)):
#         if i==0:
#             if int(s[i]) == 0:
#                 return 0
#             else:
#                 count[i] = 1
#         else:
#             now = int(s[i-1:i+1])
#             if now <= 26:
#                 if now == 0:
#                     return 0
#                 if now%10 == 0:
#                     if i > 1 and int(s[i - 2:i]) <= 26 and int(s[i - 2:i]) >= 10:
#                         count[i] = count[i - 1] - 1
#                     else:
#                         count[i] = count[i - 1]
#                 else:
#                     if now >= 10:
#                         count[i] = count[i - 1] + 1
#                     else:
#                         count[i] = count[i - 1]
#
#             else:
#                 if now%10 == 0:
#                     return 0
#                 else:
#                     count[i] = count[i - 1]
#
#     print(count)
#     return count[len(s) - 1]