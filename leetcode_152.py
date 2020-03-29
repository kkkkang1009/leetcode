# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos_result = [0 for i in range(len(nums))]
        neg_result = [0 for i in range(len(nums))]

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if i == 0:
                pos_result[i] = nums[i]
                neg_result[i] = nums[i]
            else:
                pos_result[i] = max(nums[i], nums[i] * pos_result[i - 1], nums[i] * neg_result[i - 1])
                neg_result[i] = min(nums[i], nums[i] * pos_result[i - 1], nums[i] * neg_result[i - 1])

        return max(pos_result)