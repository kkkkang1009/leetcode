# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, round(nums.__len__()/2)):
            if nums[2*i] != nums[2*i+1]:
                return nums[2*i]
        return nums[nums.__len__()-1]