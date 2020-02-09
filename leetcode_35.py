# 35. Search Insert Position

class Solution:
   def searchInsert(self, nums, target):
       i = 0
       while nums[i] < target:
           i += 1
           if i >= len(nums):
               break
       return i