# 303. Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        answer = 0
        for index in range(i, j+1):
            answer += self.nums[index]
        return answer


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)