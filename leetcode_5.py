# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            pre = i - 1
            post = i
            even = True
            while True:
                # i is Panlindrom 문장의 임시 중간 값
                # pre가 0보다 크고, post가 전체 길이 안넘어가고 값이 같을때
                if pre >= 0 and post < len(s) and s[pre] == s[post]:
                    # 중간부터 앞뒤로 한칸씩 늘려가며 중복확인
                    pre -= 1
                    post += 1
                elif even:
                    # 짝수일 경우 한번 pre를 뒤로 하나 당겨준다.
                    # 현재 최대 p보다 길다면 새로 해줌
                    if len(s[pre + 1:post]) > len(p):
                        p = s[pre + 1:post]
                    even = False
                    pre += 1
                    if s[pre: post + 1] != s[pre: post + 1][::-1]:
                        break
                    else:
                        pre -= 1
                        post += 1
                else:
                    # 더 이상 같은게 없을 때 현재 값이 p보다 크다면 변경
                    if len(s[pre + 1: post]) > len(p):
                        p = s[pre + 1: post]
                    break
            if (i + len(p) / 2) > len(s):
                break

        return p