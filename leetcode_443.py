# 443. String Compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        answer = []
        now_char = ''
        now_count = 0

        for char in chars:
            if char == now_char:
                now_count += 1
            else:
                if now_char != '':
                    answer.append(now_char)
                    if now_count > 1:
                        for num in list(str(now_count)):
                            answer.append(num)
                now_char = char
                now_count = 1
        if now_char != '':
            answer.append(now_char)
            if now_count > 1:
                for num in list(str(now_count)):
                    answer.append(num)

        for i in range(0, len(answer)):
            chars[i] = answer[i]

        for i in range(0, len(chars) - len(answer)):
            del chars[len(answer)]
        return len(chars)