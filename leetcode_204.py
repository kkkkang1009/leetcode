# 204. Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                print(i)
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum(isPrime)

# 1st - Time Limit Exceeded
# def countPrimes(self, n: int) -> int:
#     count = 1
#     if n == 0 or n == 1 or n == 2:
#         return 0
#     for i in range(3, n):
#         count += 1
#         for j in range(2, i // 2+1):
#             if i % j == 0:
#                 count -= 1
#                 break
#     return count