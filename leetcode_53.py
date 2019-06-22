# 53. Maximum Subarray
class Solution:
   def maxSubArray(self, nums: 'List[int]') -> 'int':
       max = nums[0]
       for i in range(0, len(nums)):
           sum = 0
           for j in range(i, len(nums)):
               sum += nums[j]
               if sum > max:
                   max = sum
       return max