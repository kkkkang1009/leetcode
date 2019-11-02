# 219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = False
        if len(nums) > 2:
            nums_dict = {}
            for i in range(0, len(nums)):
                if nums_dict.get(nums[i]) is None:
                    nums_dict[nums[i]] = i
                else:
                    if i - nums_dict.get(nums[i]) <= k:
                        result = True
                        break
                    else:
                        nums_dict[nums[i]] = i
        else:
            if len(nums) == 2 and nums[0] == nums[1]:
                result = True
        return result

# 1st - Time Limit Exceeded
# def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#     result = False
#     if len(nums) > 2:
#         for i in range(0, len(nums)//2):
#             print(i)
#             for j in range(0, k):
#                 if nums[i] == nums[i + k - j]:
#                     result = True
#         if not result:
#             nums.reverse()
#             for i in range(0, len(nums)//2):
#                 print(i)
#                 for j in range(0, k):
#                     if nums[i] == nums[i + k - j]:
#                         result = True
#     else:
#         if len(nums) == 2:
#             if nums[0] == nums[1]:
#                 result = True
#     return result