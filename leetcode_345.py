# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        origin = list(s)
        vowels = [0] * len(origin)
        count = 0
        for index in range(0, len(origin)):
            if s[index] == 'a' or s[index] == 'e' or s[index] == 'i' or s[index] == 'o' or s[index] == 'u' or s[
                index] == 'A' or s[index] == 'E' or s[index] == 'I' or s[index] == 'O' or s[index] == 'U':
                vowels[index] = 1
                count += 1

        front = 0
        back = len(origin) - 1

        while True:
            if vowels[front] == 0:
                front += 1
            if vowels[back] == 0:
                back -= 1

            if vowels[front] == 1 and vowels[back] == 1:
                origin[front], origin[back] = origin[back], origin[front]
                vowels[front], vowels[back] = 0, 0
                count -= 2
            if count <= 1:
                break

        return ''.join(origin)