# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        rotate = k % size
        for i in range(0, rotate):
            now = nums[size-1]
            del nums[size-1]
            nums.insert(0, now)