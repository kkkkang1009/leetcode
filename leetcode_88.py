# 88. Merge Sorted Array
class Solution:
   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       while True:
           if nums1.__len__() == m: break
           else:
               nums1.pop(len(nums1)-1)

       count = 0
       while True:
           if count == n: break
           nums1.append(nums2[0])
           nums2.pop(0)
           count += 1

       nums1.sort()