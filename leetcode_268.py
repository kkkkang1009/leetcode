# 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exist = [0]*(len(nums)+1)
        for num in nums:
            exist[num] = 1
        return exist.index(0)