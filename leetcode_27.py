# 27. Remove Element
class Solution:
   def removeElement(self, nums, val):
       i = 0
       while i < len(nums):
           if nums[i] == val:
               del nums[i]
           else:
               i += 1

       return len(nums)