# 414. Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        answer = list(set(nums))
        answer.sort()
        if len(answer) < 3:
            return answer[len(answer)-1]
        else:
            return answer[len(answer)-3]