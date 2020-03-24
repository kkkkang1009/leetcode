# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        answer = -1
        left = 1
        right = n
        while left <= right:
            guessNum = (left + right) // 2
            if guess(guessNum) == 0:
                return guessNum
            elif guess(guessNum) == 1:
                left = guessNum + 1
            elif guess(guessNum) == -1:
                right = guessNum - 1
            else:
                return -1

