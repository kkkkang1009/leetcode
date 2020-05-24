# 453. Minimum Moves to Equal Array Elements

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums)*min(nums)