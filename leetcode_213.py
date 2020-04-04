# 213. House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        def rob(nums):
            n = len(nums)
            robber = [0]*(n+1)
            robber[0] = nums[0]
            robber[1] = max(nums[0],nums[1])
            for i in range(2, n):
                robber[i] = max(robber[i-1], robber[i-2] + nums[i])
            return robber[n-1]
        return max(rob(nums[1:]), rob(nums[:-1]))