# 119. Pascal's Triangle II
import copy

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1]
        temp = copy.deepcopy(answer)
        for index in range(rowIndex+2):
            for amount in range(index):
                if amount == 0:
                    temp[0] = 1
                elif amount == index - 1:
                    temp.append(1)
                else:
                    temp[amount] = answer[amount-1]+answer[amount]
            answer = copy.deepcopy(temp)
        return answer