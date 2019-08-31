# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = False
        if len(set(nums)) != len(nums):
            check = True
        return check

# 1st - Time Limit Exceeded
# def containsDuplicate(self, nums: List[int]) -> bool:
#     check = False
#     while True:
#         if len(nums) == 0:
#             break
#         else:
#             now = nums[0]
#             nums.pop(0)
#             if now in nums:
#                 check = True
#                 break
#     return check