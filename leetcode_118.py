# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[] for row in range(numRows)]
        for index in range(numRows+1):
            for amount in range(index):
                if amount == index-1 or amount == 0:
                    answer[index-1].append(1)
                else:
                    answer[index-1].append(answer[index-2][amount-1]+answer[index-2][amount])
        return answer