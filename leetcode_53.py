# 53. Maximum Subarray
# Change scoring criteria - TimeOut
# class Solution:
#    def maxSubArray(self, nums: 'List[int]') -> 'int':
#        max = nums[0]
#        for i in range(0, len(nums)):
#            sum = 0
#            for j in range(i, len(nums)):
#                sum += nums[j]
#                if sum > max:
#                    max = sum
#        return max
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        stack = []
        list =- float('inf')
        for i in nums:
            if sum(stack) + i < i:
                stack = []
            stack.append(i)
            list = max(list, sum(stack))
        return list