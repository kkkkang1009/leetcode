# 264. Ugly Number II

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two, three, five = 0, 0, 0
        result = [1]
        while True:
            if len(result) >= n:
                break
            now_two = result[two] * 2
            now_three = result[three] * 3
            now_five = result[five] * 5
            now_min = min(now_two, now_three, now_five)
            result.append(now_min)
            if now_min == now_two:
                two += 1
            if now_min == now_three:
                three += 1
            if now_min == now_five:
                five += 1

        return result[n - 1]