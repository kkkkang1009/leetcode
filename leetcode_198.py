# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length > 2:
            robber = [0]*length
            robber[0:2] = nums[0:2]
            robber[2] = robber[0] + nums[2]
            for i in range(3, len(nums)):
                rob1 = robber[i-3] + nums[i]
                rob2 = robber[i-2] + nums[i]
                rob3 = robber[i-1]
                if rob1 > rob2:
                    robber[i] = rob1 if rob1 > rob3 else rob3
                else:
                    robber[i] = rob2 if rob2 > rob3 else rob3
            return robber[length-1]  if robber[length-1] > robber[length-2] else robber[length-2]
        else:
            big = 0
            for i in nums:
                if i > big:
                    big = i
            return big