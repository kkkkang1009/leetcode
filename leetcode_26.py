# 26. Remove Duplicates from Sorted Array
class Solution:
   def removeDuplicates(self, nums):
       i = 0
       while i < len(nums)-1:
           if nums[i] == nums[i+1]:
               del nums[i]
           else:
               i += 1
       return len(nums)