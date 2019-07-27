# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = float("inf")
        count = 0
        nums.sort()
        while nums:
            now = nums[0]
            if count < nums.count(nums[0]):
                count = nums.count(nums[0])
                major = nums[0]
            nums.reverse()
            index = len(nums)-nums.index(now)
            nums.reverse()
            nums = nums[index:]
        return major