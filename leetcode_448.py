# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res


# 1st - Time Limit Exceeded
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         if nums == []:
#             return []
#         answer = []
#         for i in range(1, len(nums) + 1):
#             try:
#                 nums.index(i)
#             except ValueError:
#                 answer.append(i)
#         return answer