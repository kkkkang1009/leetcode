# 167. Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            nowValue = numbers[i];
            needValue = target - nowValue
            if needValue in numbers[i+1:]:
                return [i+1, numbers.index(needValue, i+1, len(numbers))+1]
        return []

# 3rd - Wrong Answer
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(0, len(numbers)):
#             nowValue = numbers[i];
#             needValue = target - nowValue
#             if needValue in numbers[i + 1:]:
#                 return [i + 1, numbers[i + 1:].index(needValue) + 1]
#         return []

# 2nd - Wrong Answer
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(0, len(numbers)):
#             nowValue = numbers[i];
#             needValue = target - nowValue
#             if needValue in numbers:
#                 return [i+1, numbers.index(needValue)+1]
#         return []

# 1st - Time Limit Exceeded
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         index = len(numbers)
#         for i in range(len(numbers)):
#             if numbers[i] > target:
#                 index = i - 1
#         for i in range(index, 0, -1):
#             for j in range(0, index-1):
#                 if numbers[i] + numbers[j] == target:
#                     return [j+1, i+1]
#         return []